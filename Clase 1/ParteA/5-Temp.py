#Ejercicio 5
#Escriba un programa que transforme una temperatura ingresada por usuario
#de grados Farenheit (F) a Celsius (C), usando al siguiente fórmula:
# C = (F -32)*(5/9)

FTemp = float(input("Temp en Farenheit: "))

Ctemp = (FTemp -32)*(5/9)

print("Los ", FTemp, " F en grados Celsius son ", round(Ctemp,2), 'ºC')

