import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://yandex.com/")
print(driver.title)
time.sleep(5)