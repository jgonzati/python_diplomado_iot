#Ejercicio 4
#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

Inch = 2.54 #[cm]

num = float(input("Ingrese longitud: "))
print(round(num,1), ' [cm] = ',round(num/Inch,1), ' in')