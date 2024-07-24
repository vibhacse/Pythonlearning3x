import  requests
import pytest
import allure

@allure.title("Testcase1 - TO verify post request")
@allure.description("Verify create booking using post request")
@pytest.mark.smoke
def test_post_request1():
    base_url = "https://restful-booker.herokuapp.com/"
    path_url = "booking"
    url = base_url + path_url
    headers = {"Content-Type":"application/json"}
    payload = {
    "firstname" : "Auto_Test_First_Name",
    "lastname" : "Auto_Test_Last_Name",
    "totalprice" : 1200,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-08-01",
        "checkout" : "2024-08-02"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=url,headers=headers,json=payload)
    response.status_code == 200
    responsebody = response.json()

    Bookingid = responsebody["bookingid"]
    Firstname = responsebody["booking"]["firstname"]
    Lastname = responsebody["booking"]["lastname"]
    Totalprice = responsebody["booking"]["totalprice"]
    Depositpaid = responsebody["booking"]["depositpaid"]
    Checkindate = responsebody["booking"]["bookingdates"]["checkin"]
    Checkoutdate = responsebody["booking"]["bookingdates"]["checkout"]
    Additionalitems = responsebody["booking"]["additionalneeds"]

    assert Bookingid != 0
    assert Firstname is not None
    assert Firstname == "Auto_Test_First_Name"
    assert Lastname is not None
    assert Lastname == "Auto_Test_Last_Name"
    assert Totalprice > 0
    assert Depositpaid is not None
    assert Checkoutdate is not None
    assert Checkindate == "2024-08-01"
    assert Checkoutdate is not None
    assert Checkoutdate == "2024-08-02"
    assert Additionalitems is not None
    assert Additionalitems == "Breakfast"






