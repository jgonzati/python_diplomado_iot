#Ejercicio 2

def crear_reporte(temperatura):
	file = open('reporte.txt','w')
	for ciudad in temperatura:
		tmin, tmax = temperatura[ciudad]
		txt = '{0} : max {1}, min {2} \n'
		file.write(txt.format(ciudad, tmax, tmin))
		print(ciudad)
	file.close()

temp = {
	'Vina del mar': (9, 26), 
	'Valparaiso': (10, 24), 
	'Quilpue': (7, 30), 
	'Quintero': (4, 22)
}

crear_reporte(temp)