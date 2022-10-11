# Ejercicio 2
# En estadística descriptiva, se define el rango de un conjunto de datos
# reales como la diferencia entre el mayor y el menor de los datos.
# Escriba un programa que; (1) pregunte al usuario cuántos datos ingresará, (2) pida los datos uno por uno
# y (3) entregue como resultado el rango de los datos (suponga que todos los datos que ingrese serán válidos).

Mayor = -float('inf')
Menor = float('inf')
i = 0
Rango = 0.0
n = int(input("Ingresar n: "))

# Ingresar numeros
while i < n:
    num = float(input())

    if num > Mayor:
        Mayor = num

    if num < Menor:
        Menor = num
    i += 1
Rango = Mayor - Menor

print("El rango es: ", Rango)
