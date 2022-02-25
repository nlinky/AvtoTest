"""
Метод get_attribute
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    people_radio = browser.find_element_by_id("peopleRule")
    time.sleep(1)
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    time.sleep(1)
    robots_checked = robots_radio.get_attribute("checked")
    print("value of people radio: ", robots_checked)
    assert robots_checked is None

finally:
    time.sleep(5)
    browser.quit()
