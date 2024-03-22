import sys

numero_buscar = int (sys.arg[1])

lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista) #desordena la lista, permanente
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print("Numero encontrado")
        break
    else: 
        print (f"El elemento no se encuentra en la posicion {posicion}\n")
print ("Fuera del for")
print(f"El numero {numero_buscar} se encuantra en la posicion {posicion}")