import requests, json


def llamado_aveschile(url):
    """Extrae datos de la API mediante solicitud de get

    Args:
        url (_type_): _description_

    Returns:
        diccionario : datos de aves
    """
    url = "https://reqres.in/api/users"

    payload = ""
    headers = {}

    response = requests.get(url)
    if response.status_code == 200:
        return  response.json()
    else:
        print ("Error en la solicitud, response.status_code")
    
#if __name__ == "__main__":
