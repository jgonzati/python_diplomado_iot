#Ejercicio 2B

def cantidad(cadena, base):
    cant = 0
    for x in cadena:
        if x == base:
            cant += 1
    return cant

# -----
cadena = 'ctga ctga aatt gggc ctgg cccc'
print(cantidad(cadena, 't'))