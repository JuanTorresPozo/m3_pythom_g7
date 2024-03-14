#Juan Torres
from math import sqrt
print("Calculo de velocidad de escape") 
radio = float(input("Ingrese el radio en Km "))
print (f"El radio ingresado es {radio} [Km]")
gravedad = float(input ("Ingrese valor de graveda en m/s2 "))
print (f"El valor de gravedad ingresa es {gravedad} [m/s2]")
ve = float(2*1000*gravedad*radio)
escape = (sqrt(ve))
print(f"La velocidad de escape es {escape: .1f} [m/s]")
