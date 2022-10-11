#Ejercicio 2
#Producto Interno (producto punto)

def Prod_interno(a, b):
    n = len(a)
    i= 0
    prod = 0
    while i < n:
        prod += a[i]*b[i]
        i += 1
    return prod

# ----
a = [7,1,4,9,8]
b = range(5)

print(Prod_interno(a, b))