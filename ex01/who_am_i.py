import connector
import json
import sys
import requests

if len(sys.argv) != 2:
    print('Not enough arguments')
    exit(1)

file = open('token.out', 'r')
token = file.readline()
# print (token)
# print (file.read())

HEADERS = {'Authorization': f"Bearer {token}"}

response = requests.get('https://api.intra.42.fr/v2/users', headers=HEADERS)

users_list = response.json()
print(users_list)
needle = sys.argv[1]
print(needle)
for i in users_list:
    if needle == i['id']:
        result = i['login']
        break
    elif needle == i['login']:
        result = i['id']
        break

f = open("hello.txt", "w")
print("hello")
f.write(str(result))
f.write("hehlelel")
print("hello")
f.close()
