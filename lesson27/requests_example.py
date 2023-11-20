import requests
import json

headers = {
    "ContentType":"application/json"
}
url = 'https://swapi.dev/api'

response = requests.get(url + '/planets/', headers=headers)
print(response.json())
with open('tests_sw_planets/tatooine.json', 'w') as films:
    json.dump(response.json(), films, indent=4)
