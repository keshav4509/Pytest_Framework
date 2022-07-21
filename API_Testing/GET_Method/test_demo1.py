import json
import requests
import jsonpath

url1 = "https://simplus-mdm-uat.moreconnect.co.in/sim/api/token/"

json_value = {
    "username":"store_uat_2040",
    "password":"more2021"
    }

response = requests.post(url1, json_value )
# print(response.content)
# body_token = json.loads(response.content)
# value_token = jsonpath.jsonpath(body_token, 'access')
# value_token1 = value_token[0]
# print(value_token1)
# print(type(value_token1))

import requests


# class BearerAuth(requests.auth.AuthBase):
#     def __init__(self, token):
#         self.token = token
#
#
#     def __call__(self, r):
#         r.headers["authorization"] = "Bearer " + self.token
#         return r


url2 = 'https://simplus-mdm-uat.moreconnect.co.in/sim/api/user-details/?='
# response2 = requests.get(url2, auth=BearerAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3OTgzOTUxLCJqdGkiOiJjNmU4ODkzNGE0ZjQ0YjljODZhMGYwYzRkZDYyOWQ1NyIsInVzZXJfaWQiOiJlZGU0ZDA0ZC0zMGI3LTQ1ZTAtYTg4ZC00YWY4YjgyZGEwZGMifQ.pASB5BogLeg1oIJVc_HNJQ72TLaLHywucchvqagpjyA'))
# body_value = response2.content
# print(body_value)

auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3OTgzOTUxLCJqdGkiOiJ' \
             'jNmU4ODkzNGE0ZjQ0YjljODZhMGYwYzRkZDYyOWQ1NyIsInVzZXJfaWQiOiJlZGU0ZDA0ZC0zMGI3LTQ1ZTAtYTg4ZC00YWY4YjgyZG' \
             'EwZGMifQ.pASB5BogLeg1oIJVc_HNJQ72TLaLHywucchvqagpjyA'

hed = {'Authorization': 'Bearer ' + auth_token}
response2 = requests.get(url2, headers=hed)
print(response2.content)






