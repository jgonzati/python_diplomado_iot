#Ejercicio 6
#Escriba un programa que calcule el área de un triángulo a partir de la
#longitud de sus lados (a, b y c), y de su semiperímetro (s) mediante la siguiente fórmula:
# A = sqrt(s(s-a)(s-b)(s-c))
# s = (a+b+c)/2
import math

ladoA = int(input("Ingrese lado A: "))
ladoB = int(input("Ingrese lado B: "))
ladoC = int(input("Ingrese lado C: "))

s = (ladoA+ladoB+ladoC)/2

A = math.sqrt(s*(s-ladoA)*(s-ladoB)*(s-ladoC))

print("El Área del triangulo es: ", round(A,2))