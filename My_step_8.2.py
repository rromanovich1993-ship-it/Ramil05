import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # <-- ДОБАВЬТЕ ЭТОТ ИМПОРТ
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10, poll_frequency=1)
actions = ActionChains(driver)

driver.get("https://demoqa.com/droppable")

# 1. ДОЖДИТЕСЬ загрузки элементов (вместо мгновенного поиска)
SOURCE = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='draggable']")))
TARGET = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='droppable']")))

# 2. Прокрутите к элементу (на случай, если он вне зоны видимости)
driver.execute_script("arguments[0].scrollIntoView(true);", SOURCE)
time.sleep(0.5)  # небольшая пауза после прокрутки

# 3. Используйте drag_and_drop с дополнительным костылем для надежности
actions.drag_and_drop(SOURCE, TARGET).perform()

# 4. Проверка результата (после перетаскивания текст меняется на "Dropped!")
try:
    result = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='droppable']"), "Dropped!"))
    print("Успешно перетащили!" if result else "Не получилось")
except:
    print("Элемент не изменился")

time.sleep(3)
driver.quit()
