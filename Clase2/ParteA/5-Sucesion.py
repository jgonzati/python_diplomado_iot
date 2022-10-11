#Ejercicio 5
#A partir de un número cualquiera (entrada) es posible hacer una sucesión de números que termina en 1,
# para ello deberá seguir las siguientes instrucciones:
#- Si el número es par, se debe dividir por 2
#- Si el número es impar, se debe multiplicar por 3 y sumarle 1.

num = int(input("Ingresar numero: "))

while num != 1:
    if num%2 == 0:
        num //= 2
    else:
        num = num *3 +1
    print(num)
