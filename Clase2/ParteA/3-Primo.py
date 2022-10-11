#Ejercicio 3
#Escriba un programa que determine si un número es primo o compuesto (no primo).

count = 0
i = 2
num = int(input("Ingrese Numero: "))

while i < num:
    if num%i == 0:
        count += 1
    i += 1

if count > 0:
    print("El numero es compuesto")
else:
    print("El numero es primo")