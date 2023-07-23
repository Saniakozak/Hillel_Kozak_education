from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.remote.webelement import WebElement

absolute_path = os.path.dirname(__file__)
relative_path = "/"
full_path = os.path.join(absolute_path, relative_path)
print(f'Path: {absolute_path}')
print('Path:'+ full_path)

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("start-maximized");

driver = webdriver.Chrome(service=Service(absolute_path + '\\chromedriver.exe'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")


time.sleep(2)
driver.get("https://qauto2.forstudy.space/")

# element = driver.find_element(By.XPATH, "//*[contains(text(), 'Guest log in')]")

goButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Guest log in')]")
goButton.click()
time.sleep(2)

goButton = driver.find_element(By.XPATH, "//*[contains(text(), 'My profile')]")
goButton.click()
time.sleep(2)

assert "Logout" in driver.page_source

goButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Logout')]")
goButton.click()
time.sleep(2)

driver.close()