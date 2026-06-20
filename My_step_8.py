# Action Chains

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# добавляем ожидание уже проходили
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# добавляем Action Chains
from selenium.webdriver.common.action_chains import ActionChains



# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# подключаем ожидание
wait = WebDriverWait(driver, 10, poll_frequency=1)
# подключаем наш класс
action = ActionChains(driver)

driver.get("https://demoqa.com/buttons")

DUBLE_Clik = ("xpath", "//button[@id='doubleClickBtn']")
RIGHT_Clik = ("xpath", "//button[@id='rightClickBtn']")
# тут это локатор динамический поэтому мы находим его через метод текст
ClICK_ME = ("xpath", "//button[text()='Click Me']")

DUBLE_Clik_btn = wait.until(EC.presence_of_element_located(DUBLE_Clik))
# вызывае action


action.double_click(DUBLE_Clik_btn).perform()

time.sleep(5)
