import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/dynamic-properties")

wait = WebDriverWait(driver, 10, poll_frequency=5)

VISIBL_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

wait.until(EC.visibility_of_element_located(VISIBL_AFTER_BUTTON))

print(driver.title)


time.sleep(5)
#id="visibleAfter"