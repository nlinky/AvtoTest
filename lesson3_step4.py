"""
Задание: принимаем alert
"""
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()  # ДА
    # confirm.dismiss()  # НЕТ

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    # print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()
