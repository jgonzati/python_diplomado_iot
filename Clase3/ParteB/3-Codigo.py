#Ejercicio 3

def codigo_palabra(palabra):
    codigo = ''
    i = -1
    k = len(palabra)
    while i >= -k:
        codigo += palabra[i]
        i -= 2
    return codigo

print(codigo_palabra('axruatgrrreov'))
