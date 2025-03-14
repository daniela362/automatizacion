from selenium.webdriver.common.by import By
from Helpers.UtilitiesSelenium import *
from selenium.common.exceptions import NoSuchElementException

class Locators_sign_up:
    full_name_input_id = 'full-name'
    email_input_id = 'email'
    password_input_css = '.w-full > #password'
    repeat_password_input_css = '.w-full > #confirm-password'
    sign_up_button_css = "//button[@class='btn btn-primary']"
    assert_alert_xpath = "//div[contains(@class, 'text-sm') and contains(text(), 'Successful registration!')]"
    assert_messenger_xpath = "//label[@errors]//span[contains(text(), 'Passwords do not match')]"
    



def full_name(driver,fullName, implicit_wait=5):
    driver.implicitly_wait(implicit_wait)
    driver.find_element(By.ID,Locators_sign_up.full_name_input_id).send_keys(fullName)

def email(driver,Email):
    driver.find_element(By.ID,Locators_sign_up.email_input_id).send_keys(Email)

def password(driver,Password):
    # driver.find_element(By.CSS_SELECTOR, ".w-full > #password").send_keys("hola")
    driver.find_element(By.CSS_SELECTOR,Locators_sign_up.password_input_css).send_keys(Password)

def repeat_password(driver,repeatPassword):
    driver.find_element(By.CSS_SELECTOR,Locators_sign_up.repeat_password_input_css).send_keys(repeatPassword)

def button_sing_up(driver):
    driver.find_element(By.XPATH,Locators_sign_up.sign_up_button_css).click()

def assert_login(driver):
    try:
        driver.find_element(By.XPATH, Locators_sign_up.assert_alert_xpath)
        return True  
    except NoSuchElementException:
        return False 
    
def assert_password_no_match(driver):
    try:
        driver.find_element(By.XPATH, Locators_sign_up.assert_messenger_xpath)
        return True  
    except NoSuchElementException:
        return False 

def button_sing_up_disable(driver):
    button = driver.find_element(By.XPATH,Locators_sign_up.sign_up_button_css)