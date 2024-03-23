print("Pasos de Primeros Auxilios en caso de EMERGENCIA")
print("")
estimulo = input("¿Responde a estimulos? [s/n]").lower() 
if estimulo == "s":
    print ("Llevar a centro de urgencia mas cercano")
else:
    print("Abrir la via aerea")
    
    respira = input("¿Respira? [s/n]").lower()
    
    if respira == "s":
        print("Permitir posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a Ambulancia")
        
        ambulancia = "n"
        
        while  ambulancia == "n":
            signos = input("Tiene signos de vida [s/n]").lower()
            if signos == "s":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresion toráxica hasta que llegue la ambulancia")
                
            ambulancia = input("¿Llegó la ambulancia [s/n]")
print("Sistema de primeros auxilio terminado ")
                
            
