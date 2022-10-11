#Ejercicio 1
#Desviación Estandar
def des_estandar(valores):
    from math import sqrt
    n = len(valores)
    average = sum(valores)/n
    suma = 0
    for valor in valores:
        suma += ((valor - average)**2)
    sigma = sqrt(suma/(n-1))
    return sigma

# -----
lista = [1.3,1.3,1.3]
lista2 = [4.0,1.0,11.0,13.0,2.0,7.0]
lista3 =[1.5,9.5]
print(round(des_estandar(lista3),2))