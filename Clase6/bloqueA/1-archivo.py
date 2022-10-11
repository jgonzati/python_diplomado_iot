#Leer archivo quijote.txt

archivo = open('quijote.txt')
letras = 0
palabras = 0
lineas = 0
for linea in archivo:
    for letra in linea:
        if letra != ' ' and letra != '\n':
            letras += 1
        else:
            palabras += 1
    lineas += 1
    print(linea.strip())
print("El archivo tiene: ", letras, 'letras')
print("El archivo tiene: ", palabras, 'palabras')
print("El archivo tiene: ", lineas, 'lineas')

archivo.close()
