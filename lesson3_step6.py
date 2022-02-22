"""
Переход на новую вкладку браузера
switch_to.window
"""
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    # имя текущей вкладки
    first_window = browser.window_handles[0]
    # print(first_window)

    # имя новой вкладки
    new_window = browser.window_handles[1]
    # Переход на новую вкладку браузера
    browser.switch_to.window(new_window)

    # Текущую вкладку можно узнать так:
    current_window = browser.current_window_handle
    # print(current_window)


    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
