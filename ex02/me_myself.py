import json
import sys
import requests
import calendar
from time import sleep

if len(sys.argv) != 2:
    print('Not enough arguments')
    exit(1)

fout = open("ex02.out", 'w')
basic_uri = "https://api.intra.42.fr/v2/"

file = open('token.out', 'r')
token = file.readline()

all_data = {'app_name': 'none',
        'app_id': 'none',
        'user_id': 'none',
        'level_42': 'none',
        'level_algo_ai': 'none',
        'level_piscine': 'none',
        'pool': 'none',
        'achievements': 'none',
        'wallets': 'none',
        'correction_points': 'none'}

HEADERS = {'Authorization': f"Bearer {token}"}

def retry_task():
    """Retry the task in case of the 500 error"""
    # for i in all_data:
    #     if all_data[i] == 'none':

def month_to_num(month):
    return {'january': 1,
            'february': 2,
            'march': 3,
            'april': 4,
            'may': 5,
            'june': 6,
            'july': 7,
            'august': 8,
            'september': 9,
            'october': 10,
            'november': 11,
            'december': 12}[month]

def write_to_file(what):
    fout.write(what)

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
    if all_data['app_name'] == 'none':
        all_data['app_name'] = res.headers['X-Application-Name']
        # print(all_data['app_name'])
        all_data['app_id'] = res.headers['X-Application-Id']
        # print(all_data['app_name'])
    return res.json()

def get_user_id():
    needle = sys.argv[1]
    if needle.isdigit() == True:
        print(needle)
        all_data['user_id'] = needle
        return
    uri = basic_uri + '/users'
    users_list = make_request(uri, {'filter[login]': str(needle)})
    result = 0
    for i in users_list:
        if needle == i['login']:
            result = i['id']
            break
    all_data['user_id'] = result

def get_piscine(response):
    all_data['level_piscine'] = response['cursus_users'][0]['level']
    if all_data['level_piscine'] == '':
        all_data['level_piscine'] = 'none'
    month = response['pool_month']
    if month == '':
        month = 'none'
    year = response['pool_year']
    if year == '':
        year = 'none'
    if month != 'none':
        all_data['pool'] = str(month_to_num(month)) + ' ' + str(year)
        return
    all_data['pool'] = str(month) + ' ' + str(year)

def get_level(user_id):
    """Write the level_42 and """
    response = make_request(basic_uri + 'users/' + str(user_id))
    # print(response)
    all_data['level_42'] = response['cursus_users'][0]['level']
    all_data['wallets'] = response['wallet']
    all_data['correction_points'] = response['correction_point']
    # print(json.dumps(response, indent=4))
    all_data['achievements'] = len(response['achievements'])
    ai_level = 'none'
    for i in response['cursus_users'][0]['skills']:
        if i['name'] == 'Algorithms & AI':
            ai_level = i['level']
    all_data['level_algo_ai'] = ai_level
    return response

def main():
    get_user_id()
    response = get_level(str(all_data['user_id']))
    get_piscine(response)
    for i in all_data:
        fout.write(i + ': ')
        fout.write(str(all_data[i]) + '\n')

if __name__ == "__main__":
    main()
