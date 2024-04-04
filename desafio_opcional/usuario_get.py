import requests

url = "https://reqres.in/api/users"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

user_data=response.text

print(user_data)
for user in user_data:
    print(user)