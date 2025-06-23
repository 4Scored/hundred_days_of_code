import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

INTERNET_SPEED_URL = "https://www.speedtest.net/"

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
        pass