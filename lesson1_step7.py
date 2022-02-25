import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure")
    valuex = x.get_attribute("valuex")
    y = calc(valuex)
    #print(type(y))
    time.sleep(1)

    browser.find_element(By.ID, "answer").send_keys(y)
    time.sleep(1)

    browser.find_element(By.ID, "robotCheckbox").click()
    time.sleep(1)

    browser.find_element(By.ID, "robotsRule").click()
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
