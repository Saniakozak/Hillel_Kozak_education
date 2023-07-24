from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

driver.get("https://qauto2.forstudy.space/")

def test_text_Home():
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]")
        print("Element found")
    except NoSuchElementException:
        print("No element found")
    driver.close()