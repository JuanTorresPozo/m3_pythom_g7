import requests

url = "https://jsonplaceholder.typicode.com/posts/100"

payload = {}#datos a enviar
headers = {}#formato o tipo de dato

#response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url)

print(response.text)
print("")
print(response)#<Response [200]

if response.status_code == 200:
    #print(response.text)#convierte la respuesta en un strig
    print(response.json())#convierte la respuesta en un JSON
    respuesta = response.json() #respuesta es un diccionario que se puede manipular como tal
    print("")
    print(respuesta["title"])
    for clave, valor in respuesta.items(): 
        print(f"clave {clave} - valor {valor}") #imprimir como diccionario

else :
    print("Error en la solicitud, response.status_code")