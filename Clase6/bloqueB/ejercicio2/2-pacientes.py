#Ejercicio 2

file = open('pacientes.csv')
jovenes = open('jovenes.csv', 'w')
mayores = open('mayores.csv', 'w')

for linea in file:
    valores = linea.strip().split(';')
    if int(valores[-1]) < 30:
        jovenes.write(linea)
    if int(valores[-1]) > 60:
        mayores.write(linea)
file.close()
jovenes.close()
mayores.close()