# Ejercicio 1

file = open('notas.txt')
report = open('reporte.txt', 'w')
valores = []
for linea in file:
    valores = linea.strip().split(':')
    nombre = valores[0]
    notas = list(map(float, valores[1:]))
    prom = sum(notas) / len(notas)
    if prom >= 4.0:
        txt = '{} aprobado\n'.format(nombre)
    else:
        txt = '{} reprobado\n'.format(nombre)
    report.write(txt)
file.close()
report.close()
