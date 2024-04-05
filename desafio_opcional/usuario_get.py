import requests

url = "https://reqres.in/api/users"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
#response = requests.get
#print(response.text)

user_data=response.text

if response.status_code == 200:
    print (user_data)
    user_data = response.json
    
else:
    print("Error en la solicitud, response.status_code")
