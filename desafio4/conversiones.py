import sys

# Ingreso de datos

conversion = {
    "sol_peruano" : float(sys.argv[1]),
    "peso_argentino" : float(sys.argv[2]),
    "dolar_americano" : float(sys.argv[3]),
    "pesos_chilenos" : int(sys.argv[4]),
}

#Impresion/Calculo

print(f"Los {conversion ["pesos_chilenos"]} pesos Chilenos equivalen a:")
print (f"{conversion["sol_peruano"]*conversion["pesos_chilenos"]} Soles") 
print (f"{conversion["peso_argentino"]*conversion["pesos_chilenos"]} Pesos Argentinos") 
print (f"{conversion["dolar_americano"]*conversion["pesos_chilenos"]} Dolares Americanos") 