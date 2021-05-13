import json
import sys
import requests

# if len(sys.argv) != 2:
#     print('Not enough arguments')
#     exit(1)

file = open('token.out', 'r')
token = file.readline()

fout = open("results.txt", 'w')
HEADERS = {'Authorization': f"Bearer {token}"}

# for i in range(4):
# params = {'id': '23'}
params = {'filter[name]': 'webserv'}

id = '23'

res = requests.get('https://api.intra.42.fr/v2/projects', headers=HEADERS, params=params)
if res.status_code != 200:
    print(res.status_code)
    exit(1)
#     print(res.headers['X-Secondly-RateLimit-Remaining'])

# pages = math.ceil(int(res.headers['X-Total']) / int(res.headers['X-Per-Page']))
# print(pages)
# for i in range(pages):
#     # print(i)
#     params = {'page': str(i + 1)}
#     res = make_request(basic_uri + str(item), params)
#     res_json = res.json()
#     for i in res_json:
#         if i['name'] == item:
#             item_id = i['id']
#             break
# if item_id == 0:
#     print("There is no such element, check the campus or the project name")
#     fout.write("There is no such element, check the campus or the project name")
#     exit(0)
# # print(json.dumps(res, indent=4))
# print(item_id)
# return item_id

res_json = res.json()
for i in res.headers:
    fout.write(i + '    ' + res.headers[i] + '\n')
    # fout.write(res.headers[i])
print(res.headers)
# print(res.text)
# print(json.dumps(res_json, indent=4))
fout.write(json.dumps(res_json, indent=4))
# users_list = res.json()
# print(users_list)

# d = {'one': '1', 'two': '2'}

# for i in d:
    # print(d[i])
