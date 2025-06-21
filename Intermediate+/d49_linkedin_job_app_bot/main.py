# (in case) watch out for Linkedin blacklisting you for using bots

import os
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LINKEDIN_JOBS_URL = "https://www.linkedin.com/jobs/collections/recommended/"

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get(LINKEDIN_JOBS_URL)
sleep(5) # in case

# log in
username = driver.find_element(by=By.ID, value="username")
username.send_keys(os.environ.get("LINKEDIN_EMAIL"))
password = driver.find_element(by=By.ID, value="password")
password.send_keys(os.environ.get("LINKEDIN_PASSWORD"))
sign_in = driver.find_element(By.CSS_SELECTOR, value="div button")
sign_in.click()
sleep(5) # in case

