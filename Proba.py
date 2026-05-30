
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://avia.tutu.ru/f/Sarato")
time.sleep(2)
page_tittle = "https://avia.tutu.ru/f/Saratov"
if driver.title == page_tittle:
    print("Перешли на нужную страницу")
else:
    print(f"Ошибка текущий заголовок '{page_tittle}' не соответсвует ожиданию")
# current_1 = driver.current_url
# if current_1 == "https://avia.tutu.ru/f/Saratov":
#     print("Нужна страница")
# else:
#     print("Ошибка")

# assert driver.current_url == "https://avia.tutu.ru/f/Saratov", "Открыта неверная страница"


