"""
    Diccionarios {}
    
    estructura de datos pares de  clave:valor
    se accede a los elementos traves de la clave, no importa la posicion
    las claves no se generan automaticamente, no hay un orden
    las claves pueden ser String, numeros enteros incluso boolean
    Los balores pueden ser numericos boolean, listas, diccionarios, otro tipo de datos
    Si la clave existe modifica su valor , si la clave no existe la crea
    
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

print(len(notas))


print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}
notas["julio"] = 4
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'julio': 4}

#julio = {"nota1" : 7, "nota2" : 4}

# Modificar par clave:valor
notas["julio"] = 5
{'Camilaprint(notas)#': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'julio': 5}

#Eliminar  par clave:valor
#del notas ["FELIPE"]
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'julio': 5}
#2 forma pop() -> al eliminar, capturamos el valor
eliminado = notas.pop("Camila")
print("valor eliminado : ",eliminado)#7
print(notas)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'julio': 5}

notas2 = {
    "Mijail":2,
    "Israel":1
    
}

notas.update(notas2)
print(notas)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'julio': 5, 'Mijail': 2, 'Israel': 1}
notas2.update(notas)
print(notas2)#
#COLICIONES Al existir duplicidadde claves, se conserva