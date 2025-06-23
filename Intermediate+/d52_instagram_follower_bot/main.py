import os
from selenium import webdriver
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ.get("INSTAGRAM_USERNAME")
PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")

class InstaFollower:
    def __init__(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_opts)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()