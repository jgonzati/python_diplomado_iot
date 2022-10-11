#Trabajo Post Clase 1A

def calc_diff_goles(pais, resultados):
	diff = 0
	for rivales in resultados:
		pais0, pais1 = rivales
		if pais in rivales:
			if pais0 == pais:
				diff += resultados[rivales][0]
				diff -= resultados[rivales][1]
			else:
				diff += resultados[rivales][1]
				diff -= resultados[rivales][0]
	return diff


resultados = {
	('Honduras', 'Chile'): (0, 1),
	('Espana', 'Suiza'): (0, 1),
	('Suiza', 'Chile'): (0 ,1),
	('Espana', 'Honduras'): (3, 0),
	('Suiza', 'Honduras'): (0, 0),
	('Espana', 'Chile'): (2, 1)
}

# ----
print(calc_diff_goles('Honduras', resultados))