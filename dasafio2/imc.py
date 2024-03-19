peso = int(input("Ingrese su PESO en KILOGRAMOS :"))
estatura= int(input("Ingrese su ESTATURA en CENTIMETROS :"))
       
while estatura <= 0:
    print ("Valor de estatura INCORRECTO")    
    estatura= int(input("Ingrese su ESTATURA en CENTIMETROS :"))  
                    
#if estatura <= 0:
 #   print ("Valor de estatura INCORRECTO")
  #  estatura= int(input("Ingrese su estatura en centimetros:\n"))         
                    
imc= peso/((estatura/100)**2)

print(f"Su Indice de Masa corporal (IMC) es : {round(imc, 2)}")
if imc < 18.5:
    print("Usted clasifica según la OMS como Bajo Peso")
elif imc >= 18.5 and imc < 25:
    print("Usted clasifica según la OMS como Adecuado")
elif imc >= 25 and imc < 30:
    print("Usted clasifica según la OMS como Sobrepeso") 
elif imc >= 30 and imc < 35:
    print("Usted clasifica según la OMS como Obesidad I") 
elif imc >= 35 and imc < 40:
    print("Usted clasifica según la OMS como obesidad II") 
else: print("Usted clasifica según la OMS como obesidad III")