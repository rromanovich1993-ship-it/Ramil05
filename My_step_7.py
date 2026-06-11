        # Selenium. Check box. Radio button. Dropdown
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Для работы с Dropdown нужно импортировать ниже
from selenium.webdriver.support.select import Select

# для работы с клавиатурой импортируем keys
from selenium.webdriver.common.keys import Keys

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Check box
# driver.get("https://demoqa.com/checkbox")
# checkbox = driver.find_element(By.XPATH, "//span[@class='rc-tree-checkbox']")
# checkbox.click()
# time.sleep(2)

    # Radio button
# driver.get("https://demoqa.com/radio-button")
# YES_RADIO_BUTTON = driver.find_element(By.XPATH, "//input[@id='yesRadio']")
# IMPRESSIVE_RADIO_BUTTON = driver.find_element(By.XPATH, "//input[@id='impressiveRadio']")
# NO_RADIO_BUTTON = driver.find_element(By.XPATH, "//input[@id='noRadio']")
# YES_RADIO_BUTTON.click()

# для проверки кликабельности
# print(YES_RADIO_BUTTON.is_enabled())
# Бывает такое что селениум не может пройти через слои и чтобы пройти эти слои нужно создать парный элемент
# через парный элемент

    # Dropdown

# DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
# driver.get("https://the-internet.herokuapp.com/dropdown")
# ставим Select чтобы он раскрыл наш элемент
# dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))

# Есть три метода выбора из списка index, by_value, visible_text

# index работаем со списком index
# dropdown.select_by_index(2)

# by_value тут оталкивается от атрибута
# dropdown.select_by_value("2")

# также можно по тексту visible_text
# dropdown.select_by_visible_text("Option 1")

    # Мультесект когда выбирае не один, а сколько влезет
MULTISELECT=("xpath", "//input[@id='react-select-4-input']")
driver.get("https://demoqa.com/select-menu")
# так как вносим руками делаем через send
select = driver.find_element(*MULTISELECT)
select.send_keys("Green")

assert select.get_attribute("value") == "Green", "Error in value Green"
# после импорта с клавиатурой добавляем этот метод
select.send_keys(Keys.ENTER)


select = driver.find_element(*MULTISELECT)
select.send_keys("Blue")
assert select.get_attribute("value") == "Blue", "Error in value Blue"
select.send_keys(Keys.ENTER)


select = driver.find_element(*MULTISELECT)
select.send_keys("Red")
assert select.get_attribute("value") == "Red", "Error in value Red"
select.send_keys(Keys.ENTER)
select.send_keys(Keys.ESCAPE)
time.sleep(2)