
import os
import sys
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from page.sing_in import *
from page.sign_up import *

from Helpers.UtilitiesSelenium import *


_utilities = UtilitiesSelenium(r'C:\prueba\enviroment.config')
regist = UtilitiesSelenium.json_data('data.json')

   
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(_utilities.page_home_url)
    driver.maximize_window()
    yield driver
    driver.quit()

#CP1
def test_login_success(driver):
    email(driver,regist["registro"][0]["email"])
    password(driver,regist["registro"][0]["password"])
    sign_in(driver)
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "login_success")
    time.sleep(5)
    assert assert_login_success(driver)
    time.sleep(5)

#CP2
def test_required_fields_login(driver):
    email(driver,regist["registro"][2]["email"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "required_fields_login")
    time.sleep(5)
    button_sing_in = driver.find_element(By.XPATH,"//button [@class='btn btn-primary']")
    assert button_sing_in.get_attribute("disabled")

#CP3
def test_name_user(driver):
    username = regist["registro"][0]["full_name"]
    email(driver,regist["registro"][0]["email"])
    password(driver,regist["registro"][0]["password"])
    sign_in(driver)
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "name_user")
    time.sleep(5)
    user_welcome = driver.find_element(By.XPATH, "//h2[@class='font-bold']")
    assert username in user_welcome.text, f"Se esperaba que el saludo dijera 'Hola, {username}', pero se encontró {user_welcome.text}"

#CP4
def test_log_out(driver):
    email(driver,regist["registro"][0]["email"])
    password(driver,regist["registro"][0]["password"])
    sign_in(driver)
    time.sleep(5)
    icon_user(driver)
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "menu_log_out")
    log_out(driver)
    UtilitiesSelenium.take_screenshot(driver, "log_out")
    time.sleep(5)
    assert assert_log_out(driver)

#CP5.
def test_email_invalid_login(driver):
    email(driver,regist["registro"][7]["email"])
    password(driver,regist["registro"][7]["password"])
    UtilitiesSelenium.take_screenshot(driver, "email_invalid_login")
    sign_in(driver)
    UtilitiesSelenium.take_screenshot(driver, "email_invalid_login_sing_in")
    time.sleep(5)
    button_sing_in = driver.find_element(By.XPATH,"//button [@class='btn btn-primary']")
    assert button_sing_in.get_attribute("disabled")
