import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "http://docs.google.com/forms/d/e/1FAIpQLSeJ02bmNFuDF1Sn1_munGtVsdFT5nOgdO1DtlymzPHX9gi3wg/viewform"

header = {
    "User-Agent": "YOUR-USER-AGENT-HEADER"    
}

zillow_response = requests.get(ZILLOW_CLONE_URL, headers=header)
zillow_response.raise_for_status()
zillow_content = zillow_response.text
soup = BeautifulSoup(zillow_content, "html.parser")

all_addresses = soup.select(".StyledPropertyCardDataArea-anchor address")
addresses = [addr.get_text(strip=True) for addr in all_addresses]
# print(addresses)
all_prices = soup.select(".PropertyCardWrapper__StyledPriceLine")
prices = [price.get_text(strip=True).replace("/mo","").split("+")[0] for price in all_prices]
# print(prices)
all_links = soup.select(".StyledPropertyCardDataArea-anchor")
links = [link["href"] for link in all_links]
# print(links)

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)

for i in range(len(addresses)):
    driver.get(FORM_URL)
    sleep(2)
    address = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address.send_keys(addresses[i])
    price = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price.send_keys(prices[i])
    link = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link.send_keys(links[i])
    submit_btn = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit_btn.click()
    sleep(2)

driver.quit()




