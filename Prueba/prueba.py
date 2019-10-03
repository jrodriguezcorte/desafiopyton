import json
import requests

def request(url,api_key):
    headers = headers = {
        'cache-control': "no-cache",
        'postman-token': "f4aef68e-6ea6-af70-079c-a9304b7e42c8"
    }

    querystring = {"sol":"200","api_key": api_key}
    response = requests.request("GET", url, headers=headers, params=querystring)

    resultado = json.loads(response.text)
    return resultado

def build_web_page(diccionario):
    html = "<html>\n"
    html += "<head>\n"
    html += "</head>\n"
    html += "<body>\n"
    html += "<ul>\n"

    diccionario_fotos = diccionario['photos']
    longitud = len(diccionario_fotos)
    for i in range(longitud):
        img = diccionario_fotos[i]['img_src']
        html += "\t<li>><img src=\"{}\"></li>\n".format(img)

    html += "</ul>\n"
    html += "</body>\n"
    html += "</html>\n"

    with open("prueba.html", "w") as f:
        f.write(html)

api_key = 'rAQopkrvRyhC5hWChcJMlhkS1geKW2HeaSf7qzG4'
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100'

diccionario = request(url,api_key)
build_web_page(diccionario)
