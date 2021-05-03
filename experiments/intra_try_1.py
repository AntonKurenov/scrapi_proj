import json
import requests
# import requests_oauthlib
# from requests_oauthlib import OAuth2Session

UID = "fd16a486a7cf324ef92830dcced304aaca15f64a3370321aa7f58293cddb137a"
SECRET = "b8f5e7c17fc386c63fca9b58b367b7460164fc242aee979fd4f9aec762078017"

# req = requests.get("https://api.intra.42.fr/oauth/authorize?client_id=fd16a486a7cf324ef92830dcced304aaca15f64a3370321aa7f58293cddb137a&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2F&response_type=code")
# req = requests.get("https://api.intra.42.fr", {UID: SECRET})

url = "https://api.intra.42.fr/oauth/token"
headers = {'grant_type': 'client_credentials',
			'client_id': UID,
			'client_secret': SECRET}

req = requests.get(url, headers=headers)
# req.post("https://api.intra.42.fr/oauth/token", data={UID, SECRET})
# ken = OAuth2Session(UID, "https://api.intra.42.fr")
# https://api.intra.42.fr/oauth/token
# token = req.get_token
print(req.text)
# print(req.headers)

# oauth = O
