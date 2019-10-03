import json
import requests

def request(method,url,payload = ''):
    headers = {
        'cache-control': "no-cache",
        'postman-token': "97b55fe9-9983-9a62-068f-207803e4596e"
    }
    response = requests.request(method,url, headers=headers)

    if (method == 'GET'):
        resultado = json.loads(response.text)
        data = {'data':resultado['data']}
        return data
    if (method == 'POST' or method == 'PUT'):
        resultado = json.loads(response.text)
        return resultado
    if (method == 'DELETE'):
    #    resultado = response.status_code
        return response




url = "https://reqres.in/api/users?per_page=3"
method = 'GET'
payload = ''
json_get_data = request(method,url,payload)
print('GET')
print(json_get_data)

url = "https://reqres.in/api/users/"
method = 'POST'
payload = "{\n    \"name\": \"morpheus\",\n    \"job\": \"leader\"\n}"
json_get_data = request(method,url,payload)
print('POST')
print(request(method,url))

url = "https://reqres.in/api/users/669"
method = 'PUT'
payload = "{\n    \"name\": \"morpheus\",\n    \"job\": \"zion resident\"\n}"
json_get_data = request(method,url,payload)
print('PUT')
print(request(method,url))

url = "https://reqres.in/api/users/419"
method = 'DELETE'
payload = "{\n    \"name\": \"morpheus\",\n    \"job\": \"leader\"\n}"
json_get_data = request(method,url,payload)
print('DELETE')
print(request(method,url))
