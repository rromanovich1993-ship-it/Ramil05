import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)
# Находим нужно поле взяли для примера поле имя
# Добавляем логическую переменную где находим элемент
first_name_filed = driver.find_element(By.XPATH, "//input[@id='firstName']")
# Очищаем поле  ввода через метод
first_name_filed.clear()
# Проверяем что поле пустое
assert first_name_filed.get_attribute("value") == "", "Erorr проверить очистку имени"
# Ввод данных
first_name_filed.send_keys("Ramil")
time.sleep(2)

# Для работы с клавиатурой нужно доболнительно импортировать  (from selenium.webdriver.common.keys import Keys)
# Находим нужно поле взяли для примера поле фамилия
# Добавляем логическую переменную где находим элемент lastName
last_name_filed = driver.find_element(By.XPATH, "//input[@id='lastName']")
time.sleep(2)
# Очищаем поле  ввода через КЛАВИАТУТУ
last_name_filed.send_keys(Keys.CONTROL + "a")
last_name_filed.send_keys(Keys.BACKSPACE)
 # Проверяем что поле пустое
assert last_name_filed.get_attribute("value") == "", "Erorr проверить очистку фамилии"
last_name_filed.send_keys("Ispanov")
time.sleep(2)

time.sleep(2)
