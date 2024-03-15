import logging
from selenium import webdriver
from time import sleep
import wget
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Настройка логирования
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(filename='test_log3.txt', level=logging.INFO)

# Инициализация веб-драйвера
sbis_home = webdriver.Chrome()

sbis_home.get("https://sbis.ru")

try:
    if "https://sbis.ru" in sbis_home.current_url:
        logging.info("Ссылка ведет на страницу sbis")
    # Поиск и клик по кнопке "Контакты"
    download_button = sbis_home.find_element(By.XPATH, "//a[text()='Скачать локальные версии']")
    sbis_home.execute_script("arguments[0].scrollIntoView(true);", download_button)
    sleep(2)
    download_button.click()
    logging.info('Успешный тест: кнопка Скачать локальные версии найдена и кликнута')
    sleep(5)
    plugin = sbis_home.find_element(By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']")
    sbis_home.execute_script("arguments[0].click();", plugin)
    plugin.click()
    sleep(2)
    logging.info('Успешный тест: кнопка СБИС плагин найдена и кликнута')
    download_button2 = sbis_home.find_element(By.XPATH, '//a[contains(text(), "Скачать (Exe 8.17 МБ)")]')
    download_button2.click()
    sleep(10)
    fn = 'sbisplugin-setup-web.exe'
    dir = 'C:/Users/robov/Downloads/'
    assert os.path.isfile(dir + fn)
    logging.info('Успешный тест: установщик скачался')
    file_size = os.path.getsize(dir + fn)
    file_size_mb = round((file_size / (1024**2)),2)  
    expected_size_mb = 8,17
    logging.info(f'Фактический вес файла: {file_size_mb} Ожидаемый вес файла {expected_size_mb}')
except Exception as e:
    logging.error(f'Тест не пройден: {e}')

# Закрытие браузера
sbis_home.quit()
