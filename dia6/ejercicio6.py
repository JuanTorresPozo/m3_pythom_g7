"""
CONDICIONAL IF
Si se cumple la condicion, entonces se ejecuta el codigo

if condicion:
    #codigo a ejecutar si es verdadero
    
elif
    #

else
    #Codigo por deffaul si no se ejecuta otro codigo

"""

edad = int(input("Ingrese su edad: \n"))
if edad > 18:
    print ("Eres mayor de edad")
elif edad == 18:
    print("tiene 18 años")
else:
    print("Eres menor de edad") 
       
if edad == 0:
    print("La edad es cero")
elif edad %2 == 0:
    print("La edad es par")
else:
    print("La edad es impar")  
       
       
print("Fin del programa")