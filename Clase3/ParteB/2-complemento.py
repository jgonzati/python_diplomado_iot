#Ejercicio 2

def complementaria(cadena):
    cadena2 = cadena.replace('a','T').replace('c','G').replace('g','C').replace('t','A')
    return cadena2.lower()

#-----
cadena = 'attacgg'
c = complementaria(cadena)
print("Cadena ingresada: ", cadena)
print("Cadena complementaria: ", c)

