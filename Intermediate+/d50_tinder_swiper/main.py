import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get("https://tinder.com/")
sleep(10)

# locating facebook log-in process
allow_cookies_btn = driver.find_element(By.XPATH, value="//*[@id='u964729768']/div/div[2]/div/div/div[1]/div[1]/button")
allow_cookies_btn.click()
sleep(5)
login_btn = driver.find_element(By.CLASS_NAME, value="lxn9zzn")
login_btn.click()
sleep(5)
find_fb_login = driver.find_element(By.CLASS_NAME, value="Mend(a)")
find_fb_login.click()
sleep(5)

# facebook login
tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email = driver.find_element(By.XPATH, value="//*[@id='email']")
email.send_keys(os.environ.get("FACEBOOK_EMAIL"))
password = driver.find_element(By.XPATH, value="//*[@id='pass']")
password.send_keys(os.environ.get("FACEBOOK_PASSWORD"))
window_login_button = driver.find_element(By.XPATH, value="//*[@id='content']/div[2]/a")
window_login_button.send_keys(Keys.ENTER)

driver.switch_to.window(tinder_window)
sleep(5)

allow_location_btn = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]/span")
allow_location_btn.click()
notifications_btn = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]/span")
notifications_btn.click()

for i in range(100): 
    sleep(3)
    try:                  
        like_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
        like_button.click()    
    except ElementClickInterceptedException: # matched
        try: # check for matched popup
            match_popup = driver.find_element(By.CSS_SELECTOR, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button")
            match_popup.click()        
        except NoSuchElementException:
            sleep(5)

driver.quit()