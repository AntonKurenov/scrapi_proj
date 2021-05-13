import json
import sys
import requests
import math
from time import sleep

# if len(sys.argv) != 4:
#     print('Not enough arguments')
#     exit(1)

res_list = []

id_list = {'project_id': 0,
           'campus_id': 0}

fout = open("results.txt", 'w')
basic_uri = "https://api.intra.42.fr/v2/"

file = open('token.out', 'r')
token = file.readline()

HEADERS = {'Authorization': f"Bearer {token}"}

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

def make_request(url, params={}, count=0):
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
        sleep(2)
        count += 1
        if count == 3:
            print("Error 500 multiple times, exiting")
            exit(1)
        make_request(url, params, count)
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

def get_logins(campus_id, project_id):
    params = {'per_page': '100',
              'filter[primary_campus_id]': str(campus_id),
              'filter[project_id]': str(project_id)}
            #   'range[login]': ['a', 'z']}
    res = make_request(basic_uri + 'users', params) 
    pages = math.ceil(int(res.headers['X-Total']) / int(res.headers['X-Per-Page']))
    # print(res.text)
    # print(res.headers)
    for i in range(pages):
        params = {'page': str(i + 1),
                'per_page': '100',
                'project_id': str(project_id),
                'filter[primary_campus_id]': str(campus_id)}
        res = make_request(basic_uri + 'users', params) 
        create_list(res.json())
    print("here!")

def get_projects_and_campus_id(project, campus):
    params = {'filter[name]': project}
    res = make_request(basic_uri + 'projects', params)
    res_json = res.json()
    print(json.dumps(res_json, indent=4))
    if len(res_json) == 0:
        print("There is no such project, check the project name")
        fout.write("There is no such project, check the project name")
    id_list['project_id'] = res_json[0]['id']
    for i in res_json[0]['campus']:
        if i['name'] == campus:
            id_list['campus_id'] = i['id']
            break
    if id_list['campus_id'] == 0:
        print("There is no such campus, check the campus name")
        fout.write("There is no such campus, check the campus name")

def print_list():
    for i in range(len(res_list)):
        fout.write(res_list[i] + '\n')

def main():
    # campus_name = input("Enter campus name: ")
    # project = input("Now project: ")
    campus_name = 'Kazan'
    project = 'webserv'
    print("Ok, let's see...")
    get_projects_and_campus_id(project, campus_name)
    get_logins(str(id_list['campus_id']), str(id_list['project_id']))
    # res_list.sort(reverse=False)
    print_list()
    print("main")

if __name__ == "__main__":
    main()
