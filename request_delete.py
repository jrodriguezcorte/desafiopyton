import requests

url = "https://jsonplaceholder.typicode.com/posts/20"

headers = {
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "1e6669a7-7d56-4010-b2cd-01c5c17df71a,760aed65-d529-4dba-b834-7e335f8b131a",
    'Host': "jsonplaceholder.typicode.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "__cfduid=d4e98b1b6dabf8a7b8551a2fb94085cfd1569687841",
    'Content-Length': "0",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)
