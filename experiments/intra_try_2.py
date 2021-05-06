import json
import requests
from info import UID, SECRET

# https://api.intra.42.fr/oauth/authorize?client_id=fd16a486a7cf324ef92830dcced304aaca15f64a3370321aa7f58293cddb137a&redirect_uri=http%3A%2F%2Flocalhost%3A1919%2Fusers%2Fauth%2Fft%2Fcallback&response_type=code
# https://api.intra.42.fr/oauth/authorize?client_id=fd16a486a7cf324ef92830dcced304aaca15f64a3370321aa7f58293cddb137a&redirect_uri=https://profile.intra.42.fr&response_type=code
redirect_uri = "https://profile.intra.42.fr" 
# redirect_uri = "http://127.0.0.1" 

params = {'client_id': UID,
          'redirect_uri': redirect_uri,
          'response_type': 'code'}

response = requests.get("https://api.intra.42.fr/oauth/authorize", params=params)
if response.ok == False:
    print("an error ocurred")
    exit()

print(response.headers['status'])
print(response.headers)
print('+++++++++++++++++++++++') 
print(response.text)
# print(response.headers['code'])

if response.is_redirect == True:
    print("redirect")
    # print(res
