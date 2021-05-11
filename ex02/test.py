import json
import sys
import requests

# if len(sys.argv) != 2:
#     print('Not enough arguments')
#     exit(1)

file = open('token.out', 'r')
token = file.readline()

HEADERS = {'Authorization': f"Bearer {token}"}

# for i in range(4):
# params = {'id': '23'}
params = {'page': 2}

id = '23'

response = requests.get('https://api.intra.42.fr/v2/campus', headers=HEADERS, params=params)
if response.status_code != 200:
    print(response.status_code)
    exit(1)
#     print(response.headers['X-Secondly-RateLimit-Remaining'])

res_json = response.json()
print(response.headers)
# print(response.text)
print(json.dumps(res_json, indent=4))
# users_list = response.json()
# print(users_list)

# d = {'one': '1', 'two': '2'}

# for i in d:
    # print(d[i])
