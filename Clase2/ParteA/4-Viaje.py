#Ejercicio 4
#Un viajero desea saber cuanto tiempo tomó el viaje que realizó.
#Se ingresan las duraciones en minutos de cada uno de los tramos del viaje.
#Escriba un programa que permita ingresar los tiempos de viaje de los tramos y entregue
#como resultado el tiemop total de viaje en formato HH:MM
#El programa debe dejar de pedir tiempos cuando se ingrese un 0.

state = True
suma = 0

while state:
    tramo = int(input("Duración del tramo: "))
    if tramo != 0:
        suma += tramo
    else:
        state = False

HH = suma//60
MM = suma%60

print("Tiempo total de viaje: "+str(HH)+':'+str(MM)+' horas')