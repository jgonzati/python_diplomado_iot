#Ejercicio 3
#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona,
# y el entregue la condición de riesgo. Considere que el IMC se calcula como: peso / estatura ** 2
#El riesgo está determinado por la siguiente tabla:
#Edad < 45  y IMC < 22.0 -> Bajo
#Edad < 45  y IMC >= 22.0 -> Medio
#Edad >= 45 y IMC < 22.0 -> Medio
#Edad >= 45 y IMC >= 22.0 -> Alto

estatura = float(input("Ingrese Estatura: "))
peso = float(input("Ingrese peso: "))
edad = int(input("Ingrese Edad: "))

IMC = peso / (estatura**2)
if edad < 45 and IMC < 22.0:
    print("Bajo")
elif edad < 45 and IMC >= 22.0:
    print("Medio")
elif edad >= 45 and IMC < 22.0:
    print("Medio")
else:
    print("Alto")
