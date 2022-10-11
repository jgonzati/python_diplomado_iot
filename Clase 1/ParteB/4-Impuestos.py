#Ejercicio 4
#Escriba un programa que considere la siguiente tabla para mostrar el total
# de impuestos a pagar por una persona según su sueldo.
# X < 1000 -> 0%
# 1000 < X < 2000 -> 5%
# 2000 < X < 4000 -> 10%
# X > 4000 -> 12%

sueldo = int(input("Ingrese sueldo: "))

if sueldo < 1e3:
    print("Usted pagará 0 de impuestos")
elif sueldo < 2e3:
    print("Usted pagará ", int(sueldo*5/100), " de impuestos")
elif sueldo < 4e3:
    print("Usted pagará ", int(sueldo * 10 / 100), " de impuestos")
else:
    print("Usted pagará ", int(sueldo * 12 / 100), " de impuestos")
