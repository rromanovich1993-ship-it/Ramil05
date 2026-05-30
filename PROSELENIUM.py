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
first_name_filed = driver.find_element(By.XPATH, "//input[@id='firstName']")
first_name_filed.clear()
time.sleep(1)
first_name_filed.send_keys("Ramil")
first_name_filed.get_attribute("value")
assert first_name_filed.get_attribute("value")=="Ramil", "Error проверь это поле имя "
time.sleep(1)
Last_name_filed = driver.find_element(By.XPATH, "//input[@id='lastName']")
time.sleep(1)
Last_name_filed.send_keys(Keys.CONTROL + "a")
Last_name_filed.send_keys(Keys.BACKSPACE)
Last_name_filed.send_keys("Ispanov")
Last_name_filed.get_attribute("value")
assert Last_name_filed.get_attribute("value")=="Ispanov", "Error проверь это поле фамилия"
time.sleep(1)
email_filed = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email_filed.clear()
time.sleep(1)
email_filed.send_keys("Sobaka@mail.ru")
email_filed.get_attribute("value")
assert email_filed.get_attribute("value")== "Sobaka@mail.ru","Error проверить это поле почта"
time.sleep(1)
gender_filed = driver.find_element(By.XPATH, "//input[@value='Male']")
gender_filed.click()
time.sleep(1)
number_filed = driver.find_element(By.XPATH, "//input[@id='userNumber']")
number_filed.clear()
time.sleep(1)
number_filed.send_keys(97335343488)
time.sleep(1)
assert len(number_filed) in [10,11], "Error проверить это поле номер"
# имя //input[@id='firstName']
# фамилия //input[@id='lastName']
# почта //input[@id='userEmail']
# пол нужно выбрать //input[@value='Male']
# номер телефона //input[@id='userNumber']
# выбор дня рождения //input[@id='dateOfBirthInput']
# Выбор предмета //input[@id='subjectsInput']
# выбрать хобби //input[@id='hobbies-checkbox-1']
