#Ejercicio 2A Post Clase

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

# ----
cad = 'ctga ctga aatt gggc ctgg cccc'
cad2 = 'ctga xcga cgat ggta accc ccpc ttaa'
print(valida(cad))
print(valida(cad2))