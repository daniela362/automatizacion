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
def test_register_success(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][0]["full_name"])
    email(driver,regist["registro"][0]["email"])
    password(driver,regist["registro"][0]["password"])
    repeat_password(driver,regist["registro"][0]["password"])
    button_sing_up(driver)
    assert assert_login(driver)
    UtilitiesSelenium.take_screenshot(driver, "register_success")

#CP2
def test_name_one_word(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][1]["full_name"])
    email(driver,regist["registro"][1]["email"])
    password(driver,regist["registro"][1]["password"])
    repeat_password(driver,regist["registro"][1]["password"])
    UtilitiesSelenium.take_screenshot(driver, "name_one_word")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")


#CP3
def test_email_invalid_register(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][2]["full_name"])
    email(driver,regist["registro"][2]["email"])
    password(driver,regist["registro"][2]["password"])
    repeat_password(driver,regist["registro"][2]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "email_invalid_register")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP4



   
#CP5
def test_password_fewer_characters(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][3]["full_name"])
    email(driver,regist["registro"][3]["email"])
    password(driver,regist["registro"][3]["password"])
    repeat_password(driver,regist["registro"][3]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "password_no_requirements")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP6
def test_password_without_capital_letter(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][4]["full_name"])
    email(driver,regist["registro"][4]["email"])
    password(driver,regist["registro"][4]["password"])
    repeat_password(driver,regist["registro"][4]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "password_without_capital_letter")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP7
def test_password_without_lowercase(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][5]["full_name"])
    email(driver,regist["registro"][5]["email"])
    password(driver,regist["registro"][5]["password"])
    repeat_password(driver,regist["registro"][5]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "password_without_lowercase")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP8
def test_password_no_number(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][6]["full_name"])
    email(driver,regist["registro"][6]["email"])
    password(driver,regist["registro"][6]["password"])
    repeat_password(driver,regist["registro"][6]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "password_no_number")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP9
def test_password_no_special_character(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][3]["full_name"])
    email(driver,regist["registro"][3]["email"])
    password(driver,regist["registro"][3]["password"])
    repeat_password(driver,regist["registro"][3]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "password_no_special_character")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP10
def test_required_fields_email_empty(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][0]["full_name"])
    password(driver,regist["registro"][1]["password"])
    repeat_password(driver,regist["registro"][1]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "required_fields_email_empty")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP11
def test_required_fields_fullname_empty(driver):
    sign_up(driver)
    time.sleep(5)
    email(driver,regist["registro"][1]["email"])
    password(driver,regist["registro"][1]["password"])
    repeat_password(driver,regist["registro"][1]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "required_fields_fullname_empty")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP12
def test_required_fields_repeat_password_empty(driver):
    sign_up(driver)
    time.sleep(5)
    full_name(driver,regist["registro"][0]["full_name"])
    email(driver,regist["registro"][0]["email"])
    password(driver,regist["registro"][0]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "required_fields_repeat_password_empty")
    button_disable = driver.find_element(By.XPATH,'//button [@class="btn btn-primary" ]')
    assert button_disable.get_attribute("disabled")
    time.sleep(5)

#CP13
def test_password_no_match(driver):
    sign_up(driver)
    full_name(driver,regist["registro"][0]["full_name"])
    email(driver,regist["registro"][0]["email"])
    password(driver,regist["registro"][1]["password"])
    repeat_password(driver,regist["registro"][0]["password"])
    time.sleep(5)
    UtilitiesSelenium.take_screenshot(driver, "password_no_match")
    assert assert_password_no_match(driver)
    time.sleep(5)


