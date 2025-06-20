from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"
CHALLENGE_URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)

driver.get(CHALLENGE_URL)

# article_count = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count[1].text)
# article_count[1].click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
fname.send_keys("Firsto")
lname.send_keys("Nameo")
email.send_keys("firstonameo@yahoo.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()