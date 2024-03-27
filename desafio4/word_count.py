import sys
with open(sys.argv[1], "r") as file:
    texto=file.read()

caracteres = len(set(texto))
print(f"El numero de caracters distintos es: {caracteres}")

palabras = texto.split()
palabras = set(palabras)
print(f"El numero de palabras distintas es: {len(palabras)}")