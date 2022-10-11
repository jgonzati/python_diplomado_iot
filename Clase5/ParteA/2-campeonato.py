#Ejercicio 2

def obtener_lista_equipos(result):
    lista = []
    for equipos in result:
        for pais in equipos:
            if pais not in lista:
                lista.append(pais)
    return lista

def calcular_ptos(pais, result):
    ptos = 0
    for rivales in result:
        if pais in rivales:
            x, y = result[rivales]
            if pais == rivales[0]:
                if x > y:
                    ptos += 3
            else:
                if y > x:
                    ptos += 3
            if x == y:
                ptos += 1
    return ptos


resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

print(obtener_lista_equipos(resultados))
print(calcular_ptos('Suiza', resultados))