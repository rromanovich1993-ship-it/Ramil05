    # Selenium. XPath
# // — поиск по всему документу (начиная от корня <html>)
# / — переход на следующий уровень вложенности (например, поиск элемента внутри другого элемента

# https://hyperskill.org сайт для прмера c запросами

    # по атрибутам=97% :
# //элемент[@атрибут='значение атрибута'] пример
    # по тексту =2 %:
# //элемент[text()='текст'] пример //div[text()='Sign in']
    # по содержимому =1 %:
# //элемент[contains(@атрибут,'значение атрибута')] пример //h1[contains(@class,'text-pretty')]
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)
# Нужно  проверять все  ключевые шаги через assert
# print(driver.current_url) не обязательно принты писать
assert driver.current_url == "https://demoqa.com/automation-practice-form", "Erorr не тот сайт "
print(driver.title)
assert driver.title == "demosite", "Erorr не та страница "