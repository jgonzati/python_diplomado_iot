# Ejercicio 3
# Producto interno es cero
def Prod_interno(a, b):
    n = len(a)
    i = 0
    prod = 0
    while i < n:
        prod += a[i] * b[i]
        i += 1
    return prod


def son_ortogonales(a, b):
    return Prod_interno(a, b) == 0


# ---

a = [2, 1]
b = [-3, 6]

print(son_ortogonales(a, b))
