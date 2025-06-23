import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = 150
PROMISED_UP = 10
INTERNET_SPEED_URL = "https://www.speedtest.net/"
TWITTER_LOGIN_URL = "https://twitter.com/login"

class InternetSpeedTwitterBot:
    
    def __init__(self):
        service = Service(os.environ.get("CHROME_DRIVER_PATH"))
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):                
        self.driver.get(INTERNET_SPEED_URL)        
        sleep(5)        
        go_btn = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_btn.click()
        sleep(45)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(self.up)
        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        print(self.down)


    def tweet_at_provider(self):
        self.driver.get(TWITTER_LOGIN_URL)
        sleep(5)
        email = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        email.send_keys(os.environ.get("TWITTER_EMAIL"))
        email.send_keys(Keys.ENTER)
        sleep(5)
        password = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
        password.send_keys(os.environ.get("TWITTER_EMAIL"))
        password.send_keys(Keys.ENTER)
        sleep(20)
        tweet_create = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        tweet_create.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(5)
        tweet_btn = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div")
        tweet_btn.click()
        sleep(5)
        self.driver.quit()