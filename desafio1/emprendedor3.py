#Juan Torres
precio = float(input("Ingresar Precio de Suscripcion en CLP (Se deben ingresar solo numeros) "))
usuarios = float(input ("numero de usuarios (Se deben ingresar solo numeros) "))
gastos = float(input ("Ingresar gastos totales en CLP (Se deben ingresar solo numeros) "))
utilidad_anterior = float(input ("Ingrese utilidad totales del anio anterior en CLP (Se debe ingresar solo numeros) "))
utilidad_actual = precio*usuarios-gastos
razon = utilidad_actual/utilidad_anterior
print (f"Su utilidad es{utilidad_actual: .0f}  y su razon entre la utilidad actual y la del anio anterior es {razon: .2f}")