#Ejercicio 1
#Encontrar el Mayor

mayor = -float('inf') #Numero pequeño
i = 0
pos = 0
n = int(input("Ingrese numero de datos: "))

while i<n:
    num = int(input("Ingrese numero "+ str(i+1)+": "))
    if num > mayor:
        mayor = num
        pos = i
    i += 1
print("El mayor es el ", mayor, "que corresponde al numero ", pos+1)
