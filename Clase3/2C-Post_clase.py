#Ejercicio 2C
def valida(cadena):
    valida = True
    k = len(cadena)
    i = 0
    for x in cadena:
        if x == 'c' or x == 't' or x == 'a' or x == 'g':
            i += 1
        elif x == ' ':
            i += 1
        else:
            valida = False
    return valida and (i == k)

def cantidad(cadena, base):
    cant = 0
    for x in cadena:
        if x == base:
            cant += 1
    return cant
# ----
num = int(input("Ingresar cantidad de cadenas: "))
i = 0
cadena = []
while i < num:
    txt = "Ingresar cadena {0}: "
    cadena.append(input(txt.format(i+1)))
    i += 1
# Contadores
c_animal = 0
c_vegetal = 0
c_no_valido = 0
i = 0
while i < num:
    if valida(cadena[i]):
        suma_cg = 0
        suma_at = 0
        suma_at += cantidad(cadena[i], 'a')
        suma_at += cantidad(cadena[i], 't')
        suma_cg += cantidad(cadena[i], 'c')
        suma_cg += cantidad(cadena[i], 'g')
        if suma_cg > suma_at:
            c_vegetal += 1
        else:
            c_animal += 1
    else:
        c_no_valido += 1
    i += 1

print("Cantidad Animales: ", c_animal)
print("Cantidad Vegetales: ", c_vegetal)
print("Cantidad no validas: ", c_no_valido)