from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

COOKIE_CLICKER_URL = "https://orteil.dashnet.org/cookieclicker/"

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)

driver.get(COOKIE_CLICKER_URL)
sleep(5) # in case, could encounter captcha

lang_button = driver.find_element(by=By.ID, value="langSelect-EN")
lang_button.click()
sleep(5) # in case

big_cookie = driver.find_element(by=By.ID, value="bigCookie")
store_ids = [f"product{i}" for i in range(20)] # 1 -> 19

fin_time = time() + 60 * 10
every_five = time() + 5 # every 5 sec


keep_playing = True
while keep_playing:    
    big_cookie.click()
    
    if time() > every_five:
        curr_num_cookies = driver.find_element(by=By.ID, value="cookies")
        curr_num_cookies = int(curr_num_cookies.text.split()[0].replace(",",""))    

        avail_in_store = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']") # ids starting with 'product'

        best_product = None
        for product in avail_in_store[::-1]: # 
            if "unlocked enabled" in product.get_attribute("class"):
                best_product = product
                break

        if best_product:
            best_product.click()

    if time() > fin_time: # finish
        print(f"Final Cookie Count: {curr_num_cookies}")
        driver.close()
        # driver.quit()

