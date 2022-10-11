#Ejercicio 2

paises = {
    'Juan'  : {'Chile', 'Argentina'},
    'Pedro' : {'Francia', 'Suiza', 'Chile'},
    'Diego' : {'Chile', 'Italia', 'Francia', 'Peru'}
}

def cuantos_comun(a, b):
    cant = 0
    conj1 = paises[a]
    conj2 = paises[b]
    cant = len(conj1&conj2)
    return cant

print(cuantos_comun('Juan', 'Diego'))
print(cuantos_comun('Diego', 'Pedro'))