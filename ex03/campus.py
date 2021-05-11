import json
import sys
import requests
import math
from time import sleep

# if len(sys.argv) != 4:
#     print('Not enough arguments')
#     exit(1)

fout = open("ex03.out", 'w')
basic_uri = "https://api.intra.42.fr/v2/"

file = open('token.out', 'r')
token = file.readline()

HEADERS = {'Authorization': f"Bearer {token}"}

def retry_task():
    """Retry the task in case of the 500 error"""

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

def get_campus_id():
    campus = sys.argv[1]
    year = sys.argv[3]
    res = make_request(basic_uri + 'campus')
    res_json = res.json()
    campus_id = 0
    pages = math.ceil(res.headers['X-Total'] / res.headers['X-Per-Page'])
    for i in range(pages):
        params = {'page': str(i)}
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
    params = {'campus_id': str(campus_id),
              'pool_year': str(year)}
    res = make_request(basic_uri + 'users', params) 
    print(json.dumps(res, indent=4))

def main():
    campus_id = get_campus_id()
    print("main")

if __name__ == "__main__":
    main()
