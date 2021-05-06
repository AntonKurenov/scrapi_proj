import requests

headers = {
	"User-Agent": "alskdf"
}

response = requests.get("https://httpbin.org/get",
						headers=headers,
						params={'a': 'b', 'c': 100})

if response.ok:
	print("All went good!")

print(response.text)
