import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--incognito")
options.add_argument('--window-size=800,800')
options.page_load_strategy ="normal"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://demoqa.com/automation-practice-form")
filed_upload_filed = ("xpath","//input[@id='uploadPicture']" )

filed_filed = driver.find_element(*filed_upload_filed)

filed_filed.send_keys(r"C:\Users\MSI\PycharmProjects\Ramil05\exsmple.jpeg")

time.sleep(6)




# //input[@id='uploadPicture']

print(driver.title)
