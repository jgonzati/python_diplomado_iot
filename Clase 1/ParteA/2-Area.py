#Ejercicio 2
#Escriba un programa que determine el área de un círculo a partir de su radio.

import math

radio = int(input("Ingrese el radio de un círculo: "))

print("El área de la circunferencia es ", round(math.pi*(radio**2),2))