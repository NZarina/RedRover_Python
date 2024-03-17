# Документация API: https://restful-booker.herokuapp.com/apidoc/index.html
#
# 1. Воспроизвести все методы, рассмотренные на лекции
# 2. С помощью метода PATCH внести некоторые изменения в ранее созданную запись бронирования
# 3. Проверить, что изменения применились

import requests
import pytest


url = 'https://restful-booker.herokuapp.com/booking'


# Auth - CreateToken
# Creates a new auth token to use for access to the PUT and DELETE /booking
@pytest.fixture
def token():
    request_data = {
        "username": "admin",
        "password": "password123"}

    response = requests.post('https://restful-booker.herokuapp.com/auth', json=request_data)
    return response.json()['token']


# Booking - GetBookingIds
# Returns the ids of all the bookings that exist within the API.
# Can take optional query strings to search and return a subset of booking ids.
def get_booking_ids():
    response = requests.get(url)


# Booking - CreateBooking
# Creates a new booking in the API
def create_booking(name, surname):
    request_data = {
        "firstname": name,
        "lastname": surname,
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-08-01",
            "checkout": "2024-08-31"
        },
        "additionalneeds": "Breakfast"}

    response = requests.post(url=url, json=request_data)

    return response.json()


# Booking - GetBooking
# Returns a specific booking based upon the booking id provided
def get_booking_by_id(id_):
    response = requests.get(f'{url}/{id_}')
    return response.json()


# booking = create_booking()
# id_ = booking['bookingid']
# print(booking)
# get_booking_by_id(id_)

def test_create_booking():
    name = "Arina"
    surname = "Knyaz"

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']
    print(id_)

    new_booking = get_booking_by_id(id_)
    print(new_booking)

    assert new_booking['firstname'] == name
    assert new_booking['lastname'] == surname

# PATCH
def test_create_and_patch(token):
    name = "Petya"
    surname = "Vas"
    updated_name = "Petr"
    updated_surname = "Vasechkin"

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']
    print(id_)

    headers = {'Cookie': f'token={token}'}
    updated_data = {
        "firstname": updated_name,
        "lastname": updated_surname}

    response = requests.patch(url=f'{url}/{id_}', headers=headers, json=updated_data)
    result = response.json()

    assert response.status_code == 200
    assert result["firstname"] == updated_name
    assert result["lastname"] == updated_surname

# PUT
def test_create_and_put(token):
    name = "Alex"
    surname = "Knyaz"
    updated_surname = "Knyazev"

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']
    print(id_)

    headers = {'Cookie': f'token={token}'}
    updated_data = {
        "firstname": name,
        "lastname": updated_surname,
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-08-01",
            "checkout": "2024-08-31"
        },
        "additionalneeds": "Breakfast"}

    response = requests.put(url=f'{url}/{id_}', headers=headers, json=updated_data)
    result = response.json()

    assert response.status_code == 200
    assert result["lastname"] == updated_surname

#DELETE
def test_create_and_delete(token):
    name = "John"
    surname = "Smith"

    booking = create_booking(name=name, surname=surname)
    id_ = booking['bookingid']
    print(id_)

    headers = {'Cookie': f'token={token}'}
    get_booking_by_id(id_)
    response = requests.delete(url=f'{url}/{id_}', headers=headers)

    assert response.status_code == 201

    response2 = requests.get(f'{url}/{id_}')

    assert response2.status_code == 404



