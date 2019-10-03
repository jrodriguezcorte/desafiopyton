import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = "{\n\"title\": \"Post 101\",\n\"body\": \"Este es nuestro primer post\",\n\"userId\": 1\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "24c6de8d-9034-4c7a-aca8-1546e69406af,ecbb977e-ef9f-49d3-be68-3d5b83e6bb99",
    'Host': "jsonplaceholder.typicode.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "75",
    'Cookie': "__cfduid=d4e98b1b6dabf8a7b8551a2fb94085cfd1569687841",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
