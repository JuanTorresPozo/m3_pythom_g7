"""
 CICLO FOR   
 for variables in iterable:      
"""
#range() genera un espacio con un rango de numeros #(0,1,2,3,4,5,6,7,8,9)

for i in range (10):
    print (i)
print("")

#Rango de numeros partiendo del primero del rango hasta (n-1) #4,5,6,7,8,9
for i in range (4,10):
    print (i)
print("")

#Rango de numeros partiendo del primero del rango hasta (n-1) de 2 en 2 #4,6,8
for i in range (4,10,2):
    print (i)
print("")

""" for en javascript
for (let index = 4; index < 10; index++) {
    console.log(index);
    }
   """

print("")
#lista
numeros=[2,"4",True,3,"5", [2,5,8],{"clave":"valor"}]
for numero in numeros:
       print (numero)
            
print("")
 
 #String -> son similares a las listas
texto = "Hola Mundo"
for caracter in texto:
    print(caracter)
print("")  

#Diccionario, se componen de elementos(clave:valor)
datos_personales={
"Nombre": "Juan",
"Apellido": "Torres",
"edad": 63,
}

#imprime las claves
for clave in datos_personales:
    print(clave)#

print("")

#imprime los valores
for clave in datos_personales:
    print(datos_personales[clave])
    #print(f"clave: {clave} - valor:{valor}")#

print("")  

print("**Items**")
#imprime clave, valor   
for clave,valor in datos_personales.items():
    print(f"clave: {clave} - valor: {valor}")#  

print("**Par**")     

for par in datos_personales.items():
    print(par)#

print("")

print("**Keys**")

for clave in datos_personales.keys():
    print(clave)#
      
print("")
print("**vALUES**")
for valor in datos_personales.values():
    print(valor)#
print("")  
print("**ENUMERATE**") #ENUMERATE
for posicion, caracter in enumerate(texto):
    print(f"la posicion {posicion} del caracter {caracter}")
    
print("")
for posicion, numero in enumerate(numeros):
    print(f"la posicion {posicion} del numero {numero}")
    
print("")

#ZIP 
prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')
    
print("")
   
#BREAK
numeros=[2,"4",True,3,"5", [2,5,8],{"clave":"valor"}]
for numero in numeros:
       print (numero)
       if numero == 3:
        break
print("fuera del for")
