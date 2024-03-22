import sys, random

numero_buscar = int (sys.argv[1])

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) #desordena la lista, permanente
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print(f"El numero {numero_buscar} se encuantra en la posicion {posicion}")
        break
    else: 
        print (f"El numero no se encuentra en la posicion {posicion}\n")
print ("Fin del programa")
