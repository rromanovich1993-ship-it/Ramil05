    # Опции и загрузки и в конце Загрузка файлов
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# Все опции должны опрокидываться до драйвера

# Создаём объект из головы и достаём из него опцию
options = webdriver.ChromeOptions()
# К добавленом объекту через точку можем добавлять опции
# в данном случае добавялем опцию невидимки без интерфейса все работает под капотом(экномит память удобен для докера)
options.add_argument("--headless")

# в данном случае добавялем опцию инкогнито (не забиваются куки и запускается на чистом листе)
options.add_argument("--incognito")

# в данном случае добавялем опцию игнор сертификата безопасности (для прохождения без подтверждения)
options.add_argument("--ignore-certificate-errors")

# в данном случае добавялем опцию расширения экрана
options.add_argument("--window-size=1920,1080")


# Это Cтратегия загрузки страницы говорит Selenium  стоит ли ему ждать всех компонентов
options.page_load_strategy = "normal"
# Cтратегия загрузки страницы  говорит  Selenium  здесь ждём только html структур и ничего больше
options.page_load_strategy = "eager"




# если бы инициализация была бы норм ,то досточно было "driver = webdriver.Chrome(options=options)"

# Автоматически скачает и установит нужную версию драйвера
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager(). install()))

driver.get("https://demoqa.com/automation-practice-form")

    # Загрузка файлов
File_Upload_Filed = ("xpath", "//input[@id='uploadPicture']")
# "*" выполняет функцию распаковки верхнего кортежа
file_new = driver.find_element(*File_Upload_Filed)
file_new.send_keys(r"C:\Users\MSI\PycharmProjects\Ramil05\exsmple.jpeg")

print(driver.current_url)
print(driver.title)