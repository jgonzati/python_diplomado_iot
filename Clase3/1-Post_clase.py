#Ejercicio 1 Post Clase


# ----
num = int(input("Ingresar cant de palabras: "))
i = 0
palabra = []
while i < num:
    palabra.append(input("ingresar palabra: "))
    i += 1

print(palabra)
#contar letras
i = 0
contar = list()
while i < num:
    suma = []
    for c in palabra[i]:
        if c not in suma:
            suma.append(c)
    contar.append(len(suma))
    i += 1

print("La palabra más larga es:", palabra[contar.index(max(contar))])
print("La palabra más corta es:", palabra[contar.index(min(contar))])