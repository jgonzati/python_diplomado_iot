#Ejercicio 1
#Escriba una función que determine si un número es par o no.

def es_par(numero):
    return numero%2 == 0

#-------
num = int(input("Ingresar Numero: "))
print(es_par(num))