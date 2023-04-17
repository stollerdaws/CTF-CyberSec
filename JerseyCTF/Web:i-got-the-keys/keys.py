import requests

url = "https://jerseyctf-i-got-the-keys.chals.io/FLAG"
headers = {"authorization_key": "GdERHpBh3x"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    if "flag" in data:
        print("Flag:", data["flag"])
    else:
        print("Flag not found in the response data.")
else:
    print("Error:", response.status_code, response.text)
