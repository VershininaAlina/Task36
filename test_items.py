import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    submit_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert submit_button, "Submit button not found"
    time.sleep(10)