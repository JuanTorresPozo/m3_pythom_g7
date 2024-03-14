#Juan Torres
precio = float(input("Ingresar precio de Suscripcion en CLP (Se deben ingresar solo numeros) "))
usuario_normal = float(input ("Ingresar numero de usuarios normales (Se deben ingresar solo numeros) "))
usuario_premium = float(input ("Ingresar numero de usuarios premium (Se deben ingresar solo numeros) "))
gastos = float(input ("Ingrese gastos totales en CLP (Se deben ingresar solo numeros) "))
utilidad = (usuario_normal + 1.5*usuario_premium)*precio - gastos
utilidad = float(utilidad)
print (f"Su utilidad es{utilidad: .0f} CLS")