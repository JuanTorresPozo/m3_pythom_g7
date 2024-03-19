peso = int(input("Ingrese su peso en kgs.\n"))
estatura= int(input("Ingrese su estatura en centimetros:\n"))
       
while estatura <= 0:
    print ("Valor de estatura INCORRECTO")    
    estatura= int(input("Ingrese su estatura en centimetros:\n"))  
                    
#if estatura <= 0:
 #   print ("Valor de estatura INCORRECTO")
  #  estatura= int(input("Ingrese su estatura en centimetros:\n"))         
                    
imc= peso/((estatura/100)**2)

print(f"Su indice de >Masa corporal (Imc) es\n {round(imc, 2)}")
if imc < 18.5:
    print("Usted clasifica como bajo peso")
elif imc >= 18.5 and imc < 25:
    print("Usted clasifica como adecuado")
elif imc >= 25 and imc < 30:
    print("Usted clasifica como sobrepeso") 
elif imc >= 25 and imc < 30:
    print("Usted clasifica como sobrepeso") 
elif imc >= 30 and imc < 35:
    print("Usted clasifica como obesidad 1") 
elif imc >= 35 and imc < 40:
    print("Usted clasifica como obesidad II") 
else: print("Usted clasifica como obesidad III")