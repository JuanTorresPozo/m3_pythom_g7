#Division de numeros enteros, resulta un float
print(10/20)
print(10+ 3.5)
print(10- 3.5)
print(10* 3.5)

#STRING -> cadena de caracteres
nombre="isra"
edad="44"
numero=100
print("12345_ -!´.%")
print("")
print(edad)#imprime el contenido de la variable

#duplicacion -> solo es para los string
print(type(edad))#NameError: name 'numero' is not defined
print(3*edad)#444444
print(3*numero)

#metodo count() y len()
print("kararoto".count("a"))
print(len("13.955.160-5"))
#print(len(123456789)) TypeError: object of type 'int' has no len()

#metodo upper() mayuscula y lower()minuscula
print("kaRaRotO".upper())#KAKAROTO
print("kaRaRotO".lower())#kararoto
print("kaRaRotO".title())#Kararoto

#join -> unir elementos separados
print(", ".join(["a","b","c"]))

print(" esto es\n un mensaje")#salto de linea en un 

#tipos de datos
entero = 7
decimal = 9.5
cadena= " esto es una cadena "
booleanos = True #True o False

print(type(entero))#<class 'int'>
print(type(decimal))#<class 'float´>
print(type(cadena))#<class 'str'>
print(type(booleanos))#<clas 'boot'>

numero2 = 200
numero2 = numero2 +100

texto = "asd"
texto = texto + "" #texto = "asd "

#presicion de datos
promedio = (4+6+7)/3
print (f"el promedio es {promedio}")
print (f"el promedio es {promedio: .4f}")
print(f"resultado de la division{1/9:.2f}")
print(f"resultado de la division {round (1/9,3)}")

#Ingreso de datos (INPUT)
nombre = input("Ingrese su nombre:\n")
print(f"Tu nombre es {nombre}")
edad = input("Ingrese su edad:\n")
print(f"Tu edad es {edad}")