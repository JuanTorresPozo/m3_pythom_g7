#Juan Torres
precio = float(input("Ingresar Precio de Suscripcion en CLP (Se deben ingresar solo numeros) "))
usuarios = float(input ("Ingresar numero de usuarios (Se deben ingresar solo numeros) "))
gastos = float(input ("Ingresar gastos totales en CLP (Se deben ingresar solo numeros) "))
utilidad = precio*usuarios-gastos
print (f"Su utilidad es{utilidad: .0f} CLS")