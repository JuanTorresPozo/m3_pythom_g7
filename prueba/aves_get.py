import requests, json

def traer_aves(url):
    response = requests.get(url)
    respuesta = json.loads(response.text)
    return respuesta
    #return json,loads(requests.get(url).txt)
    
    
    
if __name__ == "__main__": 
    url = "https://aves.ninjas.cl/api/birds"
    respuesta = traer_aves(url)
    print(len(respuesta))

