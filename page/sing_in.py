from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class Locators_sign_in:
    sign_up_xpath = '//a[@class="font-bold text-primary" and contains(text(), "Sign up")]'
    sing_in_xpath = "//button [@class='btn btn-primary']"
    assert_welcome_xpath = '/html/body/app-root/app-panel-root/main/section[1]/h2'
    icon_xpath = "//div[@class='w-10 rounded-full']"
    log_out_css = "//ul[contains(@class, 'menu')]/li/a[text()='Logout']"
    assert_log_out_id = 'email'



def sign_up(driver):
    driver.find_element(By.XPATH,Locators_sign_in.sign_up_xpath).click()


def sign_in(driver):
    driver.find_element(By.XPATH,Locators_sign_in.sing_in_xpath).click()


def assert_login_success(driver):
    try:
        driver.find_element(By.XPATH, Locators_sign_in.assert_welcome_xpath)
        return True  
    except NoSuchElementException:
        return False 
    

def icon_user(driver):
    driver.find_element(By.XPATH,Locators_sign_in.icon_xpath).click()

def log_out(driver):
    driver.find_element(By.XPATH,Locators_sign_in.log_out_css).click()

def assert_log_out(driver):
    try:
        driver.find_element(By.ID, Locators_sign_in.assert_log_out_id)
        return True  
    except NoSuchElementException:
        return False 