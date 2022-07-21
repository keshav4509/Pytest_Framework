import requests
import json
import jsonpath
import pytest


def test_fetch_user_data():
    # API URL
    url = "https://reqres.in/api/users?page=2"

    # Send GET Request
    response = requests.get(url)
    print(response)
    assert str(response) == '<Response [200]>', 'Response Code is not Matching'

    # Display Response Content
    body_parsed = json.loads(response.content)  # We can use (response.text) as well to get json response.
    print(body_parsed)

    # Opening a Static json value to assert
    file = open(r'/Users/keshavsinha/pythonProject/API_Testing/Test_Data/json/user_data.json')
    data = json.load(file)
    print(data)
    assert body_parsed == data, 'Content Data is not Matching.'

    response_header = response.headers
    print(response_header)

    # Fetch value using JsonPath and it will return List value
    pages = jsonpath.jsonpath(body_parsed, 'data')
    print(pages[0][0]['email'])
    print(pages[0][0]['first_name'])
    assert pages[0][0]['email'] == 'michael.lawson@reqres.in', 'Pages email is not matching'





