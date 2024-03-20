

"""
i = 0 # 0,1,2
suma_notas = 0
while i<3:
    nota = float(input("Ingresa tu nota"))
    suma_notas = suma_notas + nota
    i += 1

print(f"el promedio de notas es: {suma_notas/3}")

"""

cant_notas = int(input("ingrese cantidad de notas\n"))
i = 0
suma_notas = 0
while i < cant_notas:
    nota = float(input(f"Ingresa tu nota {i+1} \n"))
    suma_notas = suma_notas + nota
    i += 1

print(f"el promedio de notas es: {round(suma_notas/cant_notas,2)}")


"""
saludo = "hola"
salud = Saludo + " Mundo"
print(saludo)
saludo += "chao"
print (saludo)
"""