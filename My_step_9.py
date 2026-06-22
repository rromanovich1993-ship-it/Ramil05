            # Basic Auth & Home work
# имортируем модули
import time

from selenium.webdriver import Keys
from gettext import find
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# Добавленный костыль

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

    # Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    # Добавляем ожидание и цепочку действий
wait = WebDriverWait(driver, 10, poll_frequency=1)

    # открываем страницу
driver.get("https://www.saucedemo.com")

    # Проверка  страницы
print(driver.title)
assert driver.title == "Swag Labs", "Error ошибка страницы"
time.sleep(5)
    # Определяем нужные локаторы локаторы
LOGIN_STEP = "xpath", "//input[@id='user-name']"
PASWORD_STEP = "xpath", "//input[@id='password']"
ENTER_PASSWORD_STEP = "xpath", "//input[@id='login-button']"
    # Очищаем поля методом clear
driver.find_element(*LOGIN_STEP).clear()
time.sleep(2)
    # Очищаем поля клавиатурой
driver.find_element(*PASWORD_STEP).send_keys(Keys.CONTROL + "A")
driver.find_element(*PASWORD_STEP).send_keys(Keys.BACKSPACE)
time.sleep(2)
    # ввод логина и пароля
driver.find_element(*LOGIN_STEP).send_keys("standard_user")
driver.find_element(*PASWORD_STEP).send_keys("secret_sauce")
    # проверка ввода данных
print(driver.find_element(*LOGIN_STEP).get_attribute("value"))
assert driver.find_element(*LOGIN_STEP).get_attribute("value") == "standard_user", "Erorr некорректный логин"
print(driver.find_element(*PASWORD_STEP).get_attribute("value"))
assert driver.find_element(*PASWORD_STEP).get_attribute("value") == "secret_sauce", "Erorr некорректный пароль"
    # вход
driver.find_element(*ENTER_PASSWORD_STEP).click()
time.sleep(3)

actions = ActionChains(driver)

# sort_dropdown = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
# sort_dropdown.click()
# sort_option = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']/option[@value='hilo']")
# sort_option.click()

sort_base = driver.find_element("xpath", "//select[@data-test='product-sort-container']")
sort_choice = driver.find_element("xpath", "//select[@data-test='product-sort-container']/option[@value='hilo']")
actions.move_to_element(sort_base).click().move_to_element(sort_choice).click().perform()
time.sleep(5)




