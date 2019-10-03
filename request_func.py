import json
import requests
def request(requested_url):
    headers = {
    "cache-control": "no-cache",
    'Postman-Token': "45d01907-9ff4-49f9-bb2c-348cc7fff11b,c0d4dbb5-6989-471d-811e-7292b5147f80",
    }
    response = requests.request("GET", requested_url, headers=headers)
    return json.loads(response.text)


print(request('http://jsonplaceholder.typicode.com/posts'))
