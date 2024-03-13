#esto es un comentario de una linea
print ("texto a imprimir por consola")
"""
    comentario 
    de mas de
    una linea
"""
print ("texto a imprimir por consola")
print(2+2)
print(6-2)
print(8+2)
print(2+0)
print(2+2)
print(12/5)
numero = 23
print (numero)
 
 # limitantes 
 # No esta permitido la suma de letras y numeros
#print ("texto"+12) IndentationError: unexpected indent
#print (texto",12")
#concatenar = "texto " + 12
#print ("texto"+"34")
 
#ITERPOLACION
print(f"el numero es {numero+2}")
nombre = "Mijail"
print(f"el numero es {nombre} \n y tu edad  es {numero}")
print ("Tu nombre es "+nombre)
#string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))
# formto con %: %s para string y %d numeros
print("Tu nombre  es%s y tu edad es%d" % (nombre, numero))
#metodo con cadena
apellido = "palma loren"
print (apellido.title())
