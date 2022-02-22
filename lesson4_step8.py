"""
Задание: ждем нужный текст на странице
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    # browser.implicitly_wait(5)
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")

    browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(y)

    browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    # alert.accept()

finally:
    browser.quit()
