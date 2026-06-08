         # Существуют два вида ожиданий:
    # 1. Неявные ожидания - Imlicit Waits
# Указывается один раз для всей тестовой сессии ,
#то есть работает один раз для всех тестов
#Применяется только для find_element() и find_elements()

    # 2. Явные ожидания - Explicit  wait
# Объявляется только там ,где нужно
# Ожидает нужного,конкретного какого-то
# Проверка на осутствие элемента .*
# *Это значит ,что мы можем дождаться исчезновения элемента
# если он исчезает,то всё хорошо

# Для явного ожидание нужен импорт
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


         # Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Добавляем неявное ожидание и указываем время ожидания driver.implicitly_wait(10)
# driver.implicitly_wait(10)

driver.get("https://demoqa.com/dynamic-properties")

# Создаём объект и в этот объект прикрепляем явное ожидание
wait = WebDriverWait(driver, 10, poll_frequency=10)

ENABLE_AFTER_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")
# Можно тут выбирать любой метод для ожидания из списка!
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))

time.sleep(3)