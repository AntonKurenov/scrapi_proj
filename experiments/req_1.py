import requests, json

res = requests.get("https://api.thedogapi.com/v1/images/search")

# res = requests.get("https://api.intra.42.fr/oauth/authorize?client_id=fd16a486a7cf324ef92830dcced304aaca15f64a3370321aa7f58293cddb137a&redirect_uri=https%3A%2F%2Fprofile.intra.42.fr%2F&response_type=code")
print(res.text)

resJson = res.json()
for key, value in resJson.items():
	print(key, ":", value)
# print(resJson["id"])
