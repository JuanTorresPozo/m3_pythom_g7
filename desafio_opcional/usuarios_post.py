import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "email": "george.bluth@reqres.in",
  "first_name": "Ignacio",
  "last_name": "Bluth",
  "job": "Profesor",
  "avatar": "https://reqres.in/img/faces/1-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
created_user=response.text
print(created_user)