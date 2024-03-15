import logging
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Настройка логирования
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(filename='test_log2.txt', level=logging.INFO)

# Инициализация веб-драйвера
sbis_home = webdriver.Chrome()

sbis_home.get("https://sbis.ru")

try:
    if "https://sbis.ru" in sbis_home.current_url:
        logging.info("Ссылка ведет на страницу sbis")
    # Поиск и клик по кнопке "Контакты"
    contacts_button = sbis_home.find_element(By.XPATH, "//a[text()='Контакты']")
    contacts_button.click()
    logging.info('Успешный тест: кнопка Контакты найдена и кликнута')

    element = sbis_home.find_element(By.CLASS_NAME,'sbis_ru-Region-Chooser__text')
    text = element.text

    if text == 'Республика Башкортостан':
        logging.info('Успешный тест: Подпись соответствует значению Республика Башкортостан')
    else:
        logging.info('Подпись не соответствует ожидаемому значению')

    element2 = sbis_home.find_element(By.XPATH,'//div[text()="Уфа"]')
    logging.info('Успешный тест: партнеры найдены')
    
    element.click()
    sleep(5)
    element3 = WebDriverWait(sbis_home, 20).until(
        EC.presence_of_element_located((By.XPATH,  '//span[text()="41 Камчатский край"]'))
    )
    sleep(5)
    sbis_home.execute_script("arguments[0].scrollIntoView(true);", element3)
    element3.click()
    sleep(5)
    logging.info('Успешный тест: кликнуто по Камчатский край')

    element_expected = sbis_home.find_element(By.XPATH,'//div[text()="Петропавловск-Камчатский"]')
    assert element2 != element_expected
    logging.info('Успешный тест: партнеры изменились')
    element_expected2 = sbis_home.find_element(By.CLASS_NAME,'sbis_ru-Region-Chooser__text')
    text2 = element.text
    if text2 == 'Камчатский край':
            logging.info('Успешный тест: название региона изменилось')
        
    if 'Камчатский край' in sbis_home.title:
        logging.info('Успешный тест: title - Камчатский край')
    if '41-kamchatskij-kraj' in sbis_home.current_url:
        logging.info('Успешный тест: url содержит 41-kamchatskij-kraj')

except Exception as e:
    logging.error(f'Тест не пройден: {e}')

# Закрытие браузера
sbis_home.quit()
