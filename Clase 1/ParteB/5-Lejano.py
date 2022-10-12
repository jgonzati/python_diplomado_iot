#Ejercicio 5
#Escriba un programa que permita ingresar 5 números enteros y determine
# cuál de los cuatro números es el más lejano al primero.

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))
n4 = int(input("Cuarto número: "))
n5 = int(input("Quinto número: "))

diff1 = abs(n1 - n2)
diff2 = abs(n1 - n3)
diff3 = abs(n1 - n4)
diff4 = abs(n1 - n5)

if diff1 > diff2 and diff1 > diff3 and diff1 > diff4:
    print("El número más lejano al primero número es: ", n2)
elif diff2 > diff1 and diff2 > diff3 and diff2 > diff4:
    print("El número más lejano al primero número es: ", n3)
elif diff3 > diff1 and diff3 > diff2 and diff3 > diff4:
    print("El número más lejano al primero número es: ", n4)
else:
    print("El número más lejano al primero número es: ", n5)

