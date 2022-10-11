#Ejercicio 1

from random import choice


def cadena_azar(num):
    i = 0
    s = ''
    while i < num:
        s += choice('atcg')
        i += 1
    return s

numero = int(input("Ingresar numero: "))
adn = cadena_azar(numero)

print(adn)