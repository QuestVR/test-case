import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Настройка логирования
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(filename='test_log.txt', level=logging.INFO)

# Инициализация веб-драйвера
sbis_home = webdriver.Chrome()
tensor_home = webdriver.Chrome()
sbis_home.get("https://sbis.ru")
tensor_home.get("https://tensor.ru")
url_tesnor_home = "https://tensor.ru"
about_tensor = "https://tensor.ru/about"
try:
    if "https://sbis.ru" in sbis_home.current_url:
        logging.info("Ссылка ведет на страницу sbis")
    # Поиск и клик по кнопке "Контакты"
    contacts_button = sbis_home.find_element(By.XPATH, "//a[text()='Контакты']")
    contacts_button.click()
    logging.info('Успешный тест: кнопка Контакты найдена и кликнута')
    # Поиск и клик по баннеру Тензор
    banner_element = sbis_home.find_element(By.XPATH, "//*[@id='contacts_clients']/div[1]/div/div/div[2]/div/a/img")
    banner_element.click()
    logging.info('Успешный тест: Баннер Тензор найден и кликнут')
    block_element = tensor_home.find_element(By.XPATH,"//*[@id='container']/div[1]/div/div[5]/div/div/div[1]/div/p[1]")
    logging.info('Успешный тест: Блок "Сила в людях" найден')
    about_button = tensor_home.find_element(By.CSS_SELECTOR, 'a[href="/about"].tensor_ru-link.tensor_ru-Index__link')
    tensor_home.execute_script("arguments[0].scrollIntoView();", about_button)
    about_button.click()
    logging.info('Успешный тест: кнопка "Подробнее" найдена и кликнута')
    
    assert tensor_home.current_url == "https://tensor.ru/about" 
    logging.info('Успешный тест: кнопка ведет к https://tensor.ru/about')  
    images = tensor_home.find_elements(By.CSS_SELECTOR,'.tensor_ru-About__block3-image-wrapper img')
    first_image = images[0]
    first_width = first_image.get_attribute('width')
    first_height = first_image.get_attribute('height')   
    assert all(image.get_attribute('width') == first_width and image.get_attribute('height') == first_height for image in images)
    logging.info('Все изображения равны')
except Exception as e:
    logging.error(f'Тест не пройден: {e}')

# Закрытие браузера
sbis_home.quit()
tensor_home.quit()