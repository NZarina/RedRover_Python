import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"



def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200


def test_get_booking_by_id():
    response = requests.get(f'{base_url}/1')
    response_data = response.json()
    expected_keys = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
    ]
    assert response.status_code == 200
    assert len(expected_keys) == len(response_data.keys())
    for key in expected_keys:
        assert key in response_data.keys()

def test_create_booking():
    payload = {
        "firstname": "Arina",
        "lastname": "Knyazeva",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json = payload)
    print(response.json()['bookingid'])
    assert response.status_code == 200


def test_check_created_booking(booking_id):
   result = requests.get(f"{base_url}/{booking_id}")
   print(result.json())
   assert result.status_code == 200
   assert result.json()['firstname'] == "Arina"


def test_update_booking(auth_token, booking_id):
   payload = {
       "firstname": "James",
       "lastname": "Brown",
       "totalprice": 150,
       "depositpaid": False,
       "bookingdates": {
           "checkin": "2024-01-01",
           "checkout": "2024-02-01"
       },
       "additionalneeds": "Lunch"
   }
   token = {"Cookie": f"token={auth_token}"}

   response = requests.put(f'{base_url}/{booking_id}', json=payload, headers=token)
   assert response.status_code == 200
   response_2 = requests.get(f'{base_url}/{booking_id}')
   print(response_2.json())
   assert response_2.json()["additionalneeds"] == "Lunch"

def test_delete_booking(booking_id, auth_token):
   token = {"Cookie": f"token={auth_token}"}
   response = requests.delete(f'{base_url}/{booking_id}', headers=token)
   assert response.status_code == 201
   response_get = requests.get(f'{base_url}/{booking_id}')
   assert response_get.status_code ==404



