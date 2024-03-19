from random import choice

cachipun= ["piedra", "papel", "tijera"]
computador= choice(cachipun)
# print (computador)

usuario= input("Ingresar tu jugada [piedra, papel o tijera]: ")
usuario= usuario.lower()
#print(usuario.lower())

while usuario !="piedra" and usuario != "papel" and usuario != "tijera":
    print("Jugada no valida")
    usuario= input("Ingresar tu jugada [piedra, papel o tijera]")
    
print(f"Jugaste: {usuario}")
print(f"El computador jugó: {computador}")

if usuario == "piedra" and computador == "tijera":
    print("Ganaste")
elif usuario == "papel" and computador == "piedra":
    print("GANASTE")
elif usuario == "tijera" and computador == "papel":
    print("GANASTE")
elif usuario == computador:
    print("EMPATE")
else:
    print("PERDISTE")
    
   

