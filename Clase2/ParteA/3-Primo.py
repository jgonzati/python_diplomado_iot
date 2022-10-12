#Ejercicio 3
#Escriba un programa que determine si un número es primo o compuesto (no primo).

count = 0
i = 2
num = int(input("Ingrese número: "))

while i < num:
    if num%i == 0:
        count += 1
    i += 1

if count > 0:
    print("El número es compuesto")
else:
    print("El número es primo")