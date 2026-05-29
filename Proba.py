
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://avia.tutu.ru/f/Sarato")
time.sleep(2)
print(driver.current_url)
assert driver.current_url == "https://avia.tutu.ru/f/Saratov", "Открыта неверная страница"


