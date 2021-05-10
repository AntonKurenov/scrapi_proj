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
#     response = requests.get('https://api.intra.42.fr/v2/users', headers=HEADERS)
#     print(response.headers['X-Secondly-RateLimit-Remaining'])

# users_list = response.json()
# print(users_list)

d = {'one': '1', 'two': '2'}

for i in d:
    print(d[i])
