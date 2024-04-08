import api_get, template


def crear_html(url):
    api_get.obtener_aves(url)



if __name__ =="__main__":
    url= "https://reqres.in/api/users"
    api_get.obtener_aves(url)
    
    template