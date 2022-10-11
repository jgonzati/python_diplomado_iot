#Ejercicio 1
#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario.

num = int(input("Ingrese un numero: "))
i = 0
while i < 10:
    print(str(num)+'x'+str(i+1)+' = '+str(num*(i+1)))
    i += 1
