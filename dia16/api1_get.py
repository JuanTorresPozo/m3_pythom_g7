import requests, json

url = "https://jsonplaceholder.typicode.com/posts"

payload = {}#datos a enviar
headers = {}#formato o tipo de dato

#response = requests.request("GET", url, headers=headers, data=payload)

response = requests.get(url)

print(response.text)
print("")
print(response)#<Response [200]

if response.status_code == 200:#200 OK
    print(response.text)#convierte la respuesta en un strig
    respuesta = json.loads(response.text)
    print(type(respuesta))#<class 'dict'
    for posicion,dicc in enumerate(respuesta):
        print(f"diccionario {dicc}")
        
else :
    print("Error en la solicitud, response.status_code")