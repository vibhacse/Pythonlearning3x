import allure
from selenium import webdriver


@allure.feature('browser1')
@allure.story('edge')
def test_openbrowser_edge():
    driver = webdriver.Edge()
    driver.get("https://www.google.com/")
    assert True


def test_openbrowser_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    assert True
