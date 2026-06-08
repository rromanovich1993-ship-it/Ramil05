        #User agent -это строка,которая содержит в себе информацию о клиенте
# Название и версия браузера
# Язык
# Версия ОС
# ПО установленное на используемое устройстве
# Тип устройства, с которого пользователь зашел на сайт
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Добавляем опции перед драйвером

options = webdriver.ChromeOptions()

    # Есть спецаильный сайт для User agent
    # добавяем опцию и прокидываем в неё аргумент добавляем взязытй с сайта https://useragents.ru/stable.html  User agent данные
# options.add_argument("-- user-agent = Mozilla/5.0 (Windows NT 10.0; rv:149.0) Gecko/20100101 Firefox/149.0 ")
    # Автоматически скачает и установит нужную версию драйвера
    #  и в сам драйвер прокидываем нашу опцию
# driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
# time.sleep(5)

    # Добавляем специальные три опции чтобы проходить капчу
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

    # Если вдруг этих трех опций не хватит то добавляем эту ещё одну (Зависит от винды настрок и т.д.)
    # options.add_argument("--remote-debugging-port=9222")
# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
# time.sleep(5)

    # Следующая тема Alerts (есть четыре типа Alerts)
    # 1) Первый вываливается плашка и нужно подтвердить после нажатия
    # 2) Второй который поялвяется не сразу а спустя какое-то время после нажатия
    # 3) Третий который после нажатия даёт два выбора подтверждения / отмена
    # 4) Четверты это после нажатия мы можем что-то внести и потом два выбора подтверждения / отмена
# Подклоючаем явное ожидание  перед иницаализацией (опцию можно отключить она уже не нужна)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# Создаём объект wait
wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.get("https://demoqa.com/alerts")

    # 1) Первый вываливается плашка и нужно подтвердить после нажатия

 # в данном случае не нужны глобальные переменные ,деалаем все напряму
# driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
 # Далее вызываем специальный метод switch_tu, а потом создаём переменную alert
 # тут мы использовали не явное ожидание
# alert = driver.switch_to.alert
# time.sleep(2)
 # # добавляем метод к переменной
# alert.accept()
# time.sleep(3)
 # а тут уже болле правильный вариант с явным ожидание
# alert = wait.until(EC.alert_is_present())
# time.sleep(2)
  # добавляем метод к переменной
# alert.accept()
# time.sleep(3)

    # 2) Второй который поялвяется не сразу а спустя какое-то время после нажатия

# в данном случае не нужны глобальные переменные ,деалаем все напряму
# driver.find_element(By.XPATH, "//button[@id='timerAlertButton']").click()
# alert = wait.until(EC.alert_is_present())
# time.sleep(2)
#   # добавляем метод к переменной
# alert.accept()
# time.sleep(3)

    # 3) Третий который после нажатия даёт два выбора подтверждения / отмена

# в данном случае не нужны глобальные переменные ,деалаем все напряму
# driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
# alert = wait.until(EC.alert_is_present())
# time.sleep(2)
# #   # добавляем метод к переменной accept = ок, dismiss = отклонить
# alert.dismiss()
# time.sleep(3)

    # 4) Четверты это после нажатия мы можем что-то внести и потом два выбора подтверждения / отмена

# в данном случае не нужны глобальные переменные ,деалаем все напряму
driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
alert = wait.until(EC.alert_is_present())
time.sleep(2)
#   # добавляем метод send_keys
alert.send_keys("QAQ")
time.sleep(3)
alert.accept()
time.sleep(3)