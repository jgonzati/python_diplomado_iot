#Ejercicio 2
#Escriba un programa que pida al usuario dos palabras, e indique cual de ellas es la más larga,
# y por cuantas letras lo es.

pal1 = input("Ingrese palabra 1: ")
pal2 = input("Ingrese palabra 2: ")

l1 = len(pal1)
l2 = len(pal2)
diff = abs(l1-l2)

if l1 > l2:
    print("La palabra 1 es mayor a la palabra 2, por ",diff, " caracteres")
elif l2 > l1:
    print("La palabra 2 es mayor a la palabra 1, por ", diff, " caracteres")
else:
    print("Ambas palabras tienen el mismo largo")

