import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Mini_Project#4")
@allure.description("Verify login and make appointment in health care portal")

def test_login_makeappointment():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    #Login using username and password

    username = driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    appoint_text = driver.find_element(By.TAG_NAME,"h2")
    assert appoint_text.text == "Make Appointment"

    allure.attach(driver.get_screenshot_as_png(), name='makeappointment_screenshot')



