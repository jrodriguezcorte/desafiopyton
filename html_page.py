import json
import requests
def request(requested_url):
    headers = {
    "cache-control": "no-cache",
    'Postman-Token': "45d01907-9ff4-49f9-bb2c-348cc7fff11b,c0d4dbb5-6989-471d-811e-7292b5147f80",
    }
    response = requests.request("GET", requested_url, headers=headers)
    return json.loads(response.text)


data = request("https://jsonplaceholder.typicode.com/photos")[0:10]
html = ""

for photo in data:
    html += "<img src=\"{}\">\n".format(photo["url"])

# Este recurso nos permite crear un archivo y escribir contenido en él
with open("output.html", "w") as f:
    f.write(html)
