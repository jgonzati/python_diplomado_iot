#Trabajo Personal - Ejercicio 1
#Una fundación de ayuda a la comunidad está haciendo una campaña para la recolección de dinero
# para poner máquinas de ejercicios en un parque. Para esto se considera que podría haber un total de
# N benefactores o juntar un monto total de M pesos (cualquiera de las dos condiciones se debe cumplir).

#Escriba un programa que ingrese la cantidad total de benefactores N y el monto total a recaudar M.
#Su programa debe solicitar el nombre y el monto que donará cada benefactor, uno por uno. Su programa debe
# detenerse una vez que se alcance el monto total M, o cuando se terminen de ingresar los N benefactores.

#Indique cuál es el monto mayor donado y qué benefactor lo donó.

Cbenefactores = 0
Cpesos = 0
monto = 0
montoM = 0
Nbenefactores = int(input("Ingresar la cantidad de Benefactores: "))
Mpesos = int(input("Ingresar el monto a recaudar: "))

while Cpesos < Mpesos and Cbenefactores < Nbenefactores:
    name = input("Nombre del benefactor: ")
    monto = int(input("Monto a donar: "))

    if monto > montoM:
        montoM = monto
        nameM = name
    Cpesos += monto
    Cbenefactores += 1

print("El monto mayor donado corresponde a:")
print("El benefactor ", nameM, " donó un monto de: ", montoM)