import connector
import json
import sys
import requests

if len(sys.argv) != 2:
    print('Not enough arguments')
    exit(1)

file = open('token.out', 'r')
token = file.readline()

HEADERS = {'Authorization': f"Bearer {token}"}

response = requests.get('https://api.intra.42.fr/v2/users', headers=HEADERS)

users_list = response.json()
needle = sys.argv[1]
result = 0
for i in users_list:
    if needle == i['id']:
        result = i['login']
        break
    elif needle == i['login']:
        result = i['id']
        break

f = open("ex01.out", "w")
if result == 0:
    result = "Item not found"
    print("EMPTY")
f.write(str(result))
f.close()
