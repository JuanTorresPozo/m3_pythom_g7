"""
import sys
umbral = sys.argv[1]
print (umbral)
"""
mayores_que = {}
menores_que = {}

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtrar(precios, umbral):
    filtro = {k:v for k,v in precios.items() if v > umbral}
    #mayores_que [keys] = value
    print (filtro)

    
    return filtro

filtrar(precios, 600000)





from sys import argv
precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

#python3 filtro.py 300000 menor/mayor


def filtrar(precios, umbral,mayor_que == True):
    
    
  #python3 filtro.py 300000  
  if len (argv(1)) ==2:
    filtrar(precios, umbral)
  
  else  
     #python3 filtro.py 300000 menor/mayor 
  if argv[2].lower == "mayor":
      filtrar(precios,umbral,False)
      
      
      
    filtro = []
    if opcion == 'menor':
        # Código alternativo SIN List Comprehension
        """
        for  producto in precios:
            if precios[producto] < umbral:
                filtro.append(producto)
        """
        # Código CON List Comprehension
        filtro = [producto for producto in precios if precios[producto] < umbral]
        print(f'Los productos menores al umbral son: {', '.join(filtro)}')
    elif opcion == False:
        # Código alternativo SIN List Comprehension
        """
        for  producto in precios:
            if precios[producto] > umbral:
                filtro.append(producto)
        """
        # Código CON List Comprehension
        filtro = [producto for producto in precios if precios[producto] > umbral]
        print(f'Los productos mayores al umbral son: {', '.join(filtro)}')
    else:
        print('Lo sentimos, no es una operación válida')
 umbral = int(argv[1])
if len(argv) == 3:
    opcion = argv[2]
else:
    opcion = False
filtrar(precios, umbral, opcion)       