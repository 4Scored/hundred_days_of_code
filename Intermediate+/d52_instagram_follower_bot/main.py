import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = "chefsteps"
INSTAGRAM_URL = "https://www.instagram.com/"
USERNAME = os.environ.get("INSTAGRAM_USERNAME")
PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")

class InstaFollower:
    def __init__(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_opts)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        sleep(5)
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        save_info = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_info:
            save_info.click()
        sleep(5) # precaution

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        sleep(5)    
        followers = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]") # xpath subject to change
        for _ in range(15):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            sleep(2)

    def follow(self):
        follow_btn = self.driver.find_element(By.XPATH, value="//button//div[contains(text(), 'Follow')]")
        try:
            follow_btn.click()
            sleep(2)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
            cancel_button.click()    

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()