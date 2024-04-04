import requests
import json

url = "https://reqres.in/api/users/5"

payload = json.dumps({
  "id": 5,
  "email": "charles.morris@reqres.in",
  "first_name": "Morfeo",
  "last_name": "Morris",
  "Residence": "zion",
  "avatar": "https://reqres.in/img/faces/5-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

update_user = response.text
print (update_user)
