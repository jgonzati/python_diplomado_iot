#Ejercicio Post-Clase 1B

def posiciones(resultados):
	paises = set()
	#Lista de Paises
	for rivales in resultados:
		i = 0
		while i < 2:
			paises.add(rivales[i])
			i += 1
	#Tupla de ptos
	#ptos, diff_goles, goles, pais
	t_goles = dict()
	for pais in paises:
		ptos = 0
		diff = 0
		goles = 0
		for rivales in resultados:
			if pais in rivales:
				pais0, pais1 = rivales
				#posicion
				if pais == pais0:
					if resultados[rivales][0] == resultados[rivales][1]:
						ptos += 1
					elif resultados[rivales][0] > resultados[rivales][1]:
						ptos += 3
					else:
						ptos += 0
					goles += resultados[rivales][0]
					diff += resultados[rivales][0]
					diff -= resultados[rivales][1]
				else:
					if resultados[rivales][0] == resultados[rivales][1]:
						ptos += 1
					elif resultados[rivales][1] > resultados[rivales][0]:
						ptos += 3
					else:
						ptos += 0
					goles += resultados[rivales][1]
					diff += resultados[rivales][1]
					diff -= resultados[rivales][0]
		t_goles[pais] = (ptos, goles, diff)
	lista_pos = []
	mayor = 0
	n = len(t_goles)
	lista_resultados = list(t_goles.items())
	list_temp = 0
	while n > 0 :
		i = 0
		while i < n-1:
			if lista_resultados[i][1] > lista_resultados[i+1][1]:
				list_temp = lista_resultados[i]
				lista_resultados[i] = lista_resultados[i+1]
				lista_resultados[i+1] = list_temp
			i += 1
		n -= 1
	n = len(lista_resultados)
	result = []
	while n > 0:
		result.append(lista_resultados[n-1][0])
		n -= 1
	return result

# ----
resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

print(posiciones(resultados))