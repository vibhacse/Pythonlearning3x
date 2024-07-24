import pytest
import allure

@allure.title("Testcase1 - TO verify add 1+1 == 2")
@allure.description("Testcase to verify adding function: 1+1 == 2")
@pytest.mark.smoke
def test_calcadd():
    assert 1+1 == 2

@allure.title("Testcase2 - TO verify sub 1-1 == 0")
@allure.description("Testcase to verify subraction function: 1-1 == 0")
@pytest.mark.sanity
def test_calcsub():
    assert 1-1 == 0

@allure.title("Testcase3 - TO verify mult 2*2 == 4")
@allure.description("Testcase to verify multiply function: 2*2 == 4")
@pytest.mark.regression
def test_calcmult():
    assert 2 * 2 == 4

