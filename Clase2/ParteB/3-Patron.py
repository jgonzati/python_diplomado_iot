#Ejercicio 3
#Escriba un programa que pida al usuario un valor entero n e imprima un patrón triangular
# de n líneas como el que se muestra a continuación:
# +
# ++
# +++
# ++++
# +++++
# ++++++
# +++++++

n = int(input("Ingrese n: "))
i = 1

while i <= n:
    k = i
    j = 1
    while j <= k:
        print('+', end='')
        j += 1
    print('')
    i += 1
