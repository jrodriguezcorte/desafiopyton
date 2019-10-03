import requests

url = "https://jsonplaceholder.typicode.com/posts/20"

payload = "{\n\"title\": \"Post 20\",\n\"body\": \"Este es nuestro 20 post\",\n\"userId\": 1\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d86a5f73-a3f8-4e52-82bf-c9b59726757a,b7eddf65-d33e-4087-8464-b156181a6c19",
    'Host': "jsonplaceholder.typicode.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "70",
    'Cookie': "__cfduid=d4e98b1b6dabf8a7b8551a2fb94085cfd1569687841",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
