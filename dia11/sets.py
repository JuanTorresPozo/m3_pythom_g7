"""
SETS
Conjunto de datos que no permite duplicados
no es ordenado, se escriben con {}

"""

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)
#{'Gato', 'Perro', 'Erizo de Tierra', 'Hamster', 'Tortuga', 'Hurón'}
for elemento in muchos_animales:
    print(elemento)
    
    
muchos_animales.add("Chancho")
print(muchos_animales)
#{'Erizo de Tierra', 'Tortuga', 'Perro', 'Hurón', 'Hamster', 'Chancho', 'Gato'}
muchos_animales.remove("Gato")
print(muchos_animales)
#{'Chancho', 'Hurón', 'Hamster', 'Tortuga', 'Erizo de Tierra', 'Perro'}
#muchos_animales.remove("Leon")#KeyError: 'Leon'
muchos_animales.discard("Leon")
print(muchos_animales)
muchos_animales.pop()
print(muchos_animales)
muchos_animales.clear
print(muchos_animales)#set()

print(muchos_animales.__dir__())
print("")
print(dir(muchos_animales))