# (in case) can be blacklisted for using bots
# not risking it, my attempt at this

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

LINKEDIN_JOBS_URL = "https://www.linkedin.com/jobs/collections/recommended/"
add_questions_ids = [
    "your_add_question_1",
    "your_add_question_2",
    "your_add_question_3",
    "your_add_question_4",
    "your_add_question_5"
]
work_auth_ids = [
    "work_auth_1",
    "work_auth_2"
]

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_opts)
driver.get(LINKEDIN_JOBS_URL)
sleep(5)

# log in
username = driver.find_element(by=By.ID, value="username")
username.send_keys(os.environ.get("LINKEDIN_EMAIL"))
password = driver.find_element(by=By.ID, value="password")
password.send_keys(os.environ.get("LINKEDIN_PASSWORD"))
sign_in = driver.find_element(By.CSS_SELECTOR, value="div button")
sign_in.click()
sleep(5)

# each job, assuming easy apply
job_list = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for job in job_list:
    job.click()
    sleep(3)
    
    apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
    apply.click()
    sleep(3)

    # next twice
    next_one_two = driver.find_element(by=By.ID, value="artdeco-button--next")
    next_one_two.click()
    sleep(3)
    next_one_two.click()
    sleep(3)
    
    for i in range(5): # select yes for each addition question option
        select = Select(driver.find_element(by=By.ID, value=add_questions_ids[i]))
        select.select_by_value("yes")
        sleep(2)

    select = driver.find_element(by=By.ID, value=work_auth_ids[0])
    select.click()
    select = driver.find_element(by=By.ID, value=work_auth_ids[1])
    select.click()

    review_submit = driver.find_element(by=By.CLASS_NAME, value="artdeco-button--primary")
    review_submit.click()

driver.quit()