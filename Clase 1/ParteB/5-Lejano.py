#Ejercicio 5
#Escriba un programa que permita ingresar 5 números enteros y determine
# cuál de los cuatro números es el más lejano al primero.

n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Tercer numero: "))
n4 = int(input("Cuarto numero: "))
n5 = int(input("Quinto numero: "))

diff1 = abs(n1 - n2)
diff2 = abs(n1 - n3)
diff3 = abs(n1 - n4)
diff4 = abs(n1 - n5)

if diff1 > diff2 and diff1 > diff3 and diff1 > diff4:
    print("El numero más lejano al primero numero es: ", n2)
elif diff2 > diff1 and diff2 > diff3 and diff2 > diff4:
    print("El numero más lejano al primero numero es: ", n3)
elif diff3 > diff1 and diff3 > diff2 and diff3 > diff4:
    print("El numero más lejano al primero numero es: ", n4)
else:
    print("El numero más lejano al primero numero es: ", n5)

