import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Mini_Project#4.1")
@allure.description("Verify login and make appointment in health care portal - get credentails")

def test_login_getcredentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    baseurl = "https://katalon-demo-cura.herokuapp.com/"
    driver.get(baseurl)
    make_appointment = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    #Login using username and password
    #Get username and password from text field

    username = driver.find_element(By.XPATH,"//input[@value='John Doe']")
    usernamevalue = username.get_attribute("value")
    driver.find_element(By.ID,"txt-username").send_keys(usernamevalue)
    password = driver.find_element(By.XPATH,"//input[@value='ThisIsNotAPassword']")
    passwordvalue = password.get_attribute("value")
    driver.find_element(By.ID,"txt-password").send_keys(passwordvalue)
    driver.find_element(By.ID,"btn-login").click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    appoint_text = driver.find_element(By.TAG_NAME,"h2")
    assert appoint_text.text == "Make Appointment"

    allure.attach(driver.get_screenshot_as_png(), name='makeappointment_screenshot')



