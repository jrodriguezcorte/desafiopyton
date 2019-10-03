import json
import requests

def request(method,url,payload = ''):
    headers = {
        'cache-control': "no-cache",
        'postman-token': "97b55fe9-9983-9a62-068f-207803e4596e"
    }
    if (method == 'GET'):
        url += '?per_page=3'

    response = requests.request(method,url, headers=headers)

    if (method == 'GET'):
        resultado = json.loads(response.text)
        print(resultado)
        return resultado
#        data = {'data':resultado['data']}
    if (method == 'POST' or method == 'PUT'):
        resultado = json.loads(response.text)
        print(resultado)
        return resultado
    if (method == 'DELETE'):
        print(response)
        return response
