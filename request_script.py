import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "45d01907-9ff4-49f9-bb2c-348cc7fff11b,c0d4dbb5-6989-471d-811e-7292b5147f80",
    'Host': "jsonplaceholder.typicode.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

#print(response.text)

results = json.loads(response.text)
print(type(results)) # Veremos que el resultado es una lista
print(results[0]) # Mostramos el primer elemento

print(results[0]["userId"])
print(results[0]["title"])

# ITERANDO LA lista
for post in results:
   print(post["title"])
