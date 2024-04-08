from sys import argv

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

#python filtro.py 300000 menor/mayor
umbral = int(argv[1])

def filtrar(precios, umbral, mayor_que = True):
    if mayor_que:
       # Código alternativo SIN List Comprehension
        """
        for  producto in precios:
            if precios[producto] < umbral:
                filtro.append(producto)
        """
        #Codigo con List Comprehension
        filtro = [producto for producto in precios if precios [producto] > umbral]
        print(f'Los productos mayores al umbral son: {', '.join(filtro)}')   
    else:
        # Código alternativo SIN List Comprehension
        """
        for  producto in precios:
            if precios[producto] < umbral:
                filtro.append(producto)
        """
        # Código CON List Comprehension
        filtro = [producto for producto in precios if precios[producto] < umbral]
        print(f'Los productos menores al umbral son: {', '.join(filtro)}')
   
  #python filtro.py 300000  
if len (argv) == 2:
    filtrar(precios, umbral) 
else:  
     #python3 filtro.py 300000 menor/mayor 
    if argv[2].lower() == "mayor":
        filtrar(precios,umbral)
    elif argv[2].lower() == "menor":
        filtrar(precios,umbral, False)
    else:
        print("Lo sentimos, no es una opercion valida")  
      
    