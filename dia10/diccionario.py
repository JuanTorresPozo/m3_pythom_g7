"""
    Diccionarios {}
    
    estructura de datos pares de  clave:valor
    se accede a los elementos traves de la clave, no importa la posicion
    las claves no se generan automaticamente, no hay un orden
    las claves pueden ser String, numeros enteros incluso boolean
    Los balores pueden ser numericos boolean, listas, diccionarios, otro tipo de datos
"""
diccionario = {
    1:"uno", 
    "dos":2,
    3: ["a", "b", "c"],
    "dicc": {"A": "A Mayuscula"},
    }
from os import system
#Diccionario vacio
notas = {}
print(len(notas))#cero

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
}
system("cls")
print(len(notas))
print(notas)


#Acceso a los elementos(valores)
print(notas["Camila"])
print(notas["Antonio"])
print(notas["Felipe"])
print(notas["Daniela"])
print(notas["Vicente"])
#print(notas["felipe"])#KeyError: 'felipe'
