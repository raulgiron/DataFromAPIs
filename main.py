import requests


r = requests.get("https://randomuser.me/api/?results=2")
print(r.status_code)
print(r.text)
print(r.json())
print(r.json()['results'][0]['gender'])
print(r.json()['results'][0]['name']['first'])
print(r.json()['results'][0]['location']['state'])
print(r.json()['results'][0]['email'])
print(r.json()['results'][1]['gender'])
print(r.json()['results'][1]['name']['first'])
print(r.json()['results'][1]['location']['state'])
print(r.json()['results'][1]['email'])
