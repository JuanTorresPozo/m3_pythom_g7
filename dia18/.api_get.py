import requests, json

def obtener_aves(url):

url= "https://reqres.in/api/users"
response =requests.get(url)