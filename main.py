import requests


url = 'https://restful-booker.herokuapp.com/booking'


def get_booking_by_id(id_):
    response = requests.get(f'{url}/{id_}')
    return response.json()


print(get_booking_by_id(5243))
