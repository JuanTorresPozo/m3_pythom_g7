#revisando el contenido de la API
import requests
import json
def request_get(url):
    return json.loads(requests.get(url).text)

out = request_get('https://jsonplaceholder.typicode.com/photos') [0:5]# Tomamos solo 5 datos

print(len(out))#largo del string
print(out[0].keys())#imprimiendo keys del elemento 0
print(out[0])#mprimirndo keys y value del elemnto 0
#importamos template
from string import Template 
#creamos template
img_template = Template('<img scr="$url">')
#realizamos la substitucion
imagen = img_template.substitute(url ='foto')
print (imagen)
'<img scr="foto">'

html_template = Template('''<!DOCTYPE html>
                        <html>
                        <head>
                        <title>FOTOS</title>
                        </head>
                        <body>
                        <h1>Nuestra pagina Web</h1>
                        $body
                        </body>
                        </html>
                        ''')
lista_ulr = [elemento['ulr'] for elemento in out]
texto_imagen = ""
for url in lista_ulr:
    texto_imagen += img_template.substitute(url = url)+ '\n'
print(texto_imagen)

