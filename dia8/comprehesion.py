"""
    genera los 10 primeros pares dentro de la lista
"""
n=10

lista_pares = []#lista vacia, tamaño 0
for i in range(n): #
    lista_pares.append(2*i +2)#[2,4,6,8,10,12,14,16,18,20]
    
#[formula for variable in range(n)]
lista_pares2 = [2*i +2 for i in range(n)] 
    
"""
for i in range(1,n+1): #
    lista_pares.append(2*i)#[2,4,6,8,10,12,14,16,18,20]
for i in range(2,(2*n+2),2): #
    lista_pares.append(i)#[2,4,6,8,10,12,14,16,18,20]
""" 
print(lista_pares)
print(lista_pares2)




##[expresion1 if condicion1 else expresion2 for variable]
valores = [0,4,5,7,8,9]
divisibles = []
for valor in valores:
    if valor %2 == 0:
        divisibles.append("Divisible")
    else:
        divisibles.append("No divisible")
print(divisibles)


divisibles2 = ["Divisibles" if valor % 2==0 else "No divisibl" for valor in valores ]
        
        
 ##
 
lista = ['Lechuga', "Tomates", 5, 10,True, False, True,"Papas",5.1, 45.2, 1 ,2, 0]
lista_str= []
lista_int= []
count_str= 0
for elemento in lista:
    if type(elemento) is str:
        count_str







lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))



##Diccionario Comprehesion
claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2 = {k:v for k,v in zip(claves, valores)}
print(diccionario2)