import json
import sys
import requests
import math
from time import sleep

# if len(sys.argv) != 4:
#     print('Not enough arguments')
#     exit(1)

res_list = []

fout = open("ex03.out", 'w')
basic_uri = "https://api.intra.42.fr/v2/"

file = open('token.out', 'r')
token = file.readline()

HEADERS = {'Authorization': f"Bearer {token}"}

def retry_task():
    """Retry the task in case of the 500 error"""

def num_to_month(month):
    return {1: 'january',
            2: 'february',
            3: 'march',
            4: 'april',
            5: 'may',
            6: 'june',
            7: 'july',
            8: 'august',
            9: 'september',
            10: 'october',
            11: 'november',
            12: 'december'}[month]

def make_request(url, params={}):
    res = requests.get(url=url, headers=HEADERS, params=params)
    if res.status_code == 429:
        if res.headers['X-Hourly-RateLimit-Remaining'] == '0':
            sleep(res.headers['Retry-after'])
        sleep(2)
        res = requests.get(url=url, headers=HEADERS, params=params)
    elif res.status_code >= 400 and res.status_code <= 499:
        print(res.status_code)
        exit(1)
    elif res.status_code == 500:
        retry_task()
    # print(res.headers)
    return res

def create_list(res_json):
    """Get the logins and put them in list"""
    # print("hello")
    size = len(res_list)
    size_json = len(res_json)
    print(size_json)
    for i in range(size_json):
        res_list.append(res_json[i]['login'])

def get_logins(campus_id):
    year = sys.argv[3]
    if str(sys.argv[2]).isdigit() == True:
        print("true")
        month = num_to_month(int(sys.argv[2]))
    params = {'per_page': '100',
              'filter[primary_campus_id]': str(campus_id),
              'filter[pool_year]': str(year),
              'filter[pool_month]': str(month)}
            #   'range[login]': ['a', 'z']}
    res = make_request(basic_uri + 'users', params) 
    pages = math.ceil(int(res.headers['X-Total']) / int(res.headers['X-Per-Page']))
    # print(res.text)
    # print(res.headers)
    for i in range(pages):
        params = {'page': str(i + 1),
                'per_page': '100',
                'filter[primary_campus_id]': str(campus_id),
                'filter[pool_year]': str(year),
                'filter[pool_month]': str(month)}
        res = make_request(basic_uri + 'users', params) 
        create_list(res.json())
    print("here!")

def get_campus_id():
    campus = sys.argv[1]
    res = make_request(basic_uri + 'campus')
    res_json = res.json()
    campus_id = 0
    pages = math.ceil(int(res.headers['X-Total']) / int(res.headers['X-Per-Page']))
    print(pages)
    for i in range(pages):
        # print(i)
        params = {'page': str(i + 1)}
        res = make_request(basic_uri + 'campus', params)
        res_json = res.json()
        for i in res_json:
            if i['name'] == campus:
                campus_id = i['id']
                break
    if campus_id == 0:
        print("There is no such campus")
        fout.write("There is no such campus")
        exit(0)
    # print(json.dumps(res, indent=4))
    print(campus_id)
    return campus_id
    # print(json.dumps(res, indent=4))

def print_list():
    for i in range(len(res_list)):
        fout.write(res_list[i] + '\n')

def main():
    campus_id = get_campus_id()
    get_logins(campus_id)
    res_list.sort(reverse=False)
    print_list()
    print("main")

if __name__ == "__main__":
    main()
