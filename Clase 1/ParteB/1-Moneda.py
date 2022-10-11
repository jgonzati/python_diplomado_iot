#Ejercicio 1
#Escriba un programa que genere aleatoriamente el lanzamiento de una moneda
# y muestre por pantalla su resultado (CARA o SELLO).

import random

moneda = random.randint(0,1)

if moneda > 0:
    print("Cara")
else:
    print("Sello")
