# Request
# Method - Get request - Booking ID
# URL - https://restful-booker.herokuapp.com/booking/111
# Auth - NA
# Payload - NA
# Content-type- or header - NA
# Query param - NA
# Path param - 111

# Response
# Verify Body(Key/Values), Status Code, Time, JSON/XML schema

# Add request module to this project

import  requests
import pytest
import allure

@allure.title("Testcase1 - TO verify get request with valid booking id")
@allure.description("Given valid booking id - positive case")
@pytest.mark.smoke
def test_get_request_bookingid_valid():
    url = "https://restful-booker.herokuapp.com/booking/111"
    responsedata = requests.get(url)
    print(responsedata.json())
    assert responsedata.status_code == 200

@allure.title("Testcase2 - TO verify get request with invalid booking id")
@allure.description("Given invalid booking id - negative case")
@pytest.mark.smoke
def test_get_request_bookingid_valid():
    url = "https://restful-booker.herokuapp.com/booking/11100"
    responsedata = requests.get(url)
    #print(responsedata.json()) --> Not required as 404 does not contains response body
    assert responsedata.status_code == 404