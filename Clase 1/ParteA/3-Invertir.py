#Ejercicio 3
#Escriba un programa que invierta un número entero de tres dígitos.

num = int(input("Ingrese un número: "))

digito = str(num%10)
num = num//10
digito = digito+str(num%10)
num = num // 10
digito = digito + str(num%10)
print("El número invertido es: "+digito)

