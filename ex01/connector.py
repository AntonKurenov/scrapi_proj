import json
import requests
from info import UID, SECRET

# redirect_uri = "https://httpbin.org/anything" 

params = {'grant_type': 'client_credentials',
          'client_id': UID,
          'client_secret': SECRET}

def connect():
    response = requests.post("https://api.intra.42.fr/oauth/token", params=params)
    if response.ok == False:
        print("an error ocurred")
        exit()
    resp_json = response.json()
    print(resp_json['access_token'])
