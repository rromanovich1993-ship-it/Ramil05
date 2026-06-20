import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10, poll_frequency=1)
actions = ActionChains(driver)
driver.get("https://demoqa.com/menu")


STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

# также создаём переменные куда кладем распаковку наших локаторов
STEP_1 = driver.find_element(*STEP_1_LOCATOR)
STEP_2 = driver.find_element(*STEP_2_LOCATOR)
STEP_3 = driver.find_element(*STEP_3_LOCATOR)

# Добавляем метотд наведения
# также есть возможность поставить в методе pause(2)

actions.move_to_element(STEP_1).pause(3).move_to_element(STEP_2).move_to_element(STEP_3).perform()
time.sleep(3)