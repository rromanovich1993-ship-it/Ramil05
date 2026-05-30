import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/automation-practice-form")
# time.sleep(2)
print(driver.title)
assert driver.current_url == "https://demoqa.com/automation-practice-form", "ERROR проверьте стартовую страницу"

# имя //input[@id='firstName']
first_name_filed = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name_filed.clear()
time.sleep(1)
first_name_filed.send_keys("Ramil")
first_name_filed.get_attribute("value")
assert first_name_filed.get_attribute("value")=="Ramil", "Error проверь это поле имя "
time.sleep(1)

# фамилия //input[@id='lastName']
Last_name_filed = driver.find_element(By.XPATH, "//input[@id='lastName']")
time.sleep(1)
Last_name_filed.send_keys(Keys.CONTROL + "a")
Last_name_filed.send_keys(Keys.BACKSPACE)
Last_name_filed.send_keys("Ispanov")
Last_name_filed.get_attribute("value")
assert Last_name_filed.get_attribute("value")=="Ispanov", "Error проверь это поле фамилия"
time.sleep(1)

# почта //input[@id='userEmail']
email_filed = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email_filed.clear()
time.sleep(1)
email_filed.send_keys("Sobaka@mail.ru")
email_filed.get_attribute("value")
assert email_filed.get_attribute("value")== "Sobaka@mail.ru","Error проверить это поле почта"
time.sleep(1)

# пол нужно выбрать //input[@value='Male']
gender_filed = driver.find_element(By.XPATH, "//input[@value='Male']")
gender_filed.click()
time.sleep(1)

# номер телефона //input[@id='userNumber']
number_filed = driver.find_element(By.XPATH, "//input[@id='userNumber']")
number_filed.clear()
time.sleep(1)
number_filed.send_keys(Keys.CONTROL + "a")
number_filed.send_keys(Keys.BACKSPACE)
number_filed.send_keys("9733534348")
number_filed.get_attribute("value")
time.sleep(1)
assert number_filed.get_attribute("value") == "9733534348","Error проверить это поле номер"

# выбор дня рождения //input[@id='dateOfBirthInput']
happy_day_failed = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")

time.sleep(1)
# Удаляем атрибут readonly через JavaScript
driver.execute_script("arguments[0].removeAttribute('readonly')", happy_day_failed)
time.sleep(1)
# Очищаем поле
happy_day_failed.clear()
time.sleep(1)
# Вводим дату
happy_day_failed.send_keys("05.09.1993")
time.sleep(1)
# Нажимаем Enter для подтверждения
happy_day_failed.send_keys(Keys.ENTER)
time.sleep(3)
# Проверяем ввод
assert happy_day_failed.get_attribute("value") == "05 Sep 1993", "Error проверь это поле дата"


# имя //input[@id='firstName']
# фамилия //input[@id='lastName']
# почта //input[@id='userEmail']
# пол нужно выбрать //input[@value='Male']
# номер телефона //input[@id='userNumber']
# выбор дня рождения //input[@id='dateOfBirthInput']
# Выбор предмета //input[@id='subjectsInput']
# выбрать хобби //input[@id='hobbies-checkbox-1']
