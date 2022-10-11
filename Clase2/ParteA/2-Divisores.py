#Ejercicio 2
#Escribir programa que entregue todos los divisores de un número entero ingresado.
#Su programa deberá validar que el número ingresado sea positivo (>0)

state = True

while state:
    num = int(input("Ingrese un numero: "))
    if num > 0:
        state = False
    else:
        print("Error, debe ingresar un numero mayor a 0")

i = 1

while i <= num:
    if num%i == 0:
        print(i, end=' ')
    i += 1
