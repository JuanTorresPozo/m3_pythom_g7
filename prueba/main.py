import aves_get, template


def crear_html(url):
    response = aves_get.traer_aves(url)
    acumulador = "" 
    for dicc in response:
        #titulo_esp = dicc["name"]["spanish"]
        #titulo_en = dicc["name"]["english"]
        #url_img = dicc["images"]["full"]
        #print(titulo_esp,titulo_en, url_img)
        acumulador = acumulador + template.aves.substitute(titulo_esp = dicc["name"]["spanish"],
                                        titulo_en = dicc["name"]["english"],
                                        url_img = dicc["images"]["full"])
        
    return template.html.substitute(contenido = acumulador)

if __name__ == "__main__":
    url=  "https://aves.ninjas.cl/api/birds"
    #aves_get.traer_aves
    
    html = crear_html(url)
    print(type(template.html))
    
    archivo = open("index2.html","w")
    archivo.write(html)
    