import json
import sys
import requests
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

def write_to_file(what):
    fout.write(what)

def make_request(url, params={}):
    res = requests.get(url=url, headers=HEADERS, params=params)
    if res.status_code == 429:
        if res.headers['X-Hourly-RateLimit-Remaining'] == '0':
            sleep(res.headers['Retry-after'])
        sleep(2)
        res = requests.get(url=url, headers=HEADERS, params=params)
    elif res.status_code >= 400 && res.status_code <= 499:
        print(res.status_code)
    elif res.status_code == 500:
        retry_task()
    if all_data['app_name'] == 'none':
        all_data['app_name'] = res.headers['X-Application-Name']
        print(all_data['app_name'])
        all_data['app_id'] = res.headers['X-Application-Id']
        print(all_data['app_name'])
    return res.json()

# Get the name of the app:
def get_app_name():
    response = make_request('https://api.intra.42.fr/oauth/token/info')
    app_uid = response['application']['uid']
    print(app_uid)
    response = make_request(basic_uri + '/apps/', {'filter[uid]': app_uid}) #str(app_id)})
    write_to_file("app_name: " + str(response) + '\n')

def get_app_id():
    return res

def get_user_id():
    needle = sys.argv[1]
    write_to_file('user_id: ')
    if needle.isdigit == True:
        write_to_file(str(needle))
        return
    uri = basic_uri + '/users'
    users_list = make_request(uri)
    result = 0
    for i in users_list:
        if needle == i['login']:
            result = i['id']
            break
    write_to_file(str(result))
    return result

def get_level(user_id):
    """Write the level_42 and """
    write_to_file("level_42: ")
    response = make_request(basic_uri + 'users/' + str(user_id))
    print(response)
    write(str(response['cursus_users']['level']))
    write(

def main():
    get_app_name()
    user_id = get_user_id()
    get_level(user_id)

if __name__ == "__main__":
    main()

# f = open("ex01.out", "w")
# if result == 0:
#     result = "Item not found"
# f.write(str(result))
# f.close()
