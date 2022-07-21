import requests
import json
import jsonpath
import pytest



# API URL
url = "https://reqres.in/api/users/2"

# Send DELETE Request
response = requests.delete(url)

# Fetch Response Code
status_code = response.status_code
print(status_code)
assert status_code == 204, 'Status Code is not Matching.'


