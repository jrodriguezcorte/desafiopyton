import json
import requests
def request(requested_url):
    payload = ""
    headers = {
    "cache-control": "no-cache",
    "app_id": "1f9ff7ad",
    "app_key": "2200ad470d2af9829349a0ee38e44424",
    }

    response = requests.request("GET", requested_url, data=payload, headers=headers)
    return json.loads(response.text)

word = "Apple"
result = request("https://od-api.oxforddictionaries.com:443/api/v2/entries/en/{}".format(word))
result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']

print(result)
