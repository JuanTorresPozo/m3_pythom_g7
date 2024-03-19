edad = 27

# ¿Juan eed mayor de edad?
print(edad >= 18) # true
print(edad <=18 ) # false

# ¿Juan se graduo del colegio antes de los 18 años?
edad_graduacion_colegio = 17
print (edad_graduacion_colegio < 18)#true
print (edad_graduacion_colegio == 18)#false
print (edad_graduacion_colegio > 18)#false
print (edad_graduacion_colegio >= 18)#false ->mayor o igual

#¿Juan no tiene 4 años de experiencia laboral?
experiencia_laboral = 4
print(experiencia_laboral !=4)#false
print(experiencia_laboral ==4)#true
print(experiencia_laboral < 4 or experiencia_laboral > 4)#false

#¿Juan tiene hijos?
numero_hijos = 0
print (numero_hijos > 0)#false
print (numero_hijos < 1)#True
print (numero_hijos == 0)#true
print (numero_hijos != 0)#false

nombre= "Mijail"

#comparacion entre = y ==

me_llamo_juan= (nombre =="Juan")#false; true


""" edad > 18 y duracion_pololeo > 0

P = edad > 18
Q = duracion_pololeo > 0

p = T ; p = F
q = T ; q = F
R

cantidad de combinaciones
2^2= 4
2^3= 8

y (and) -> si ambas son verdaderas, el resultado es verdaddero (TRUE)

P Q AND
V V  V *
V F  F
F V  F
F F  F
--------------------
o (or) -> si ambas son falsas, todo el resultado es falso 

P Q  OR
V V  V 
V F  V
F V  V
F F  F *

"""
# soy estudiantes y ingreso a clases todos los dias
# True and False -> False

# me gusta comes fruta o me gusta comer verduras
# True or True -> True

# ser o no ser
# True or False -> True

-(-(-V))=
-(-F)
-V
False
