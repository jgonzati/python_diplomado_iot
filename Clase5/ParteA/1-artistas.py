#Ejercicio 1 Parte A

def cantidad_de_artistas(day):
    cant = len(artistas_por_dia[day])
    return cant

def nombre_primer_artista(day):
    code = artistas_por_dia[day][0]
    for nombre, presentacion in artistas.items():
        if presentacion[0] == code:
            name = nombre
    return name

def pais_origen_ultimo(day):
    code_last = artistas_por_dia[day][-1]
    for value in artistas.values():
        if value[0] == code_last:
            pais = value[1]
    return pais

def tiempo_total(day):
    time = 0
    codes = artistas_por_dia[day]
    for cc in codes:
        for code,_,min in artistas.values():
            if cc == code:
                time += min

    return time

artistas = {
    # nombre: codigo, origen, duracion en minutos de la presentacion)
    'Marco Antonio Solis': (1, 'Estados Unidos', 74),
    'Daddy Yankee': (2, 'Puerto Rico', 70),
    'Myriam Hernandez': (3, 'Chile', 40),
    'Los Charros de Lumaco': (4, 'Chile', 25),
    'Metallica': (5, 'Estados Unidos', 45),
    'U2': (6, 'Irlanda', 80),
    'Justin Bieber': (7, 'Canada', 5),
}

artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1, 4, 3, 6, 2, 5),
    "Martes": (2, 5, 1),
    "Miercoles": (3, 6, 2, 4),
    "Jueves": (2, 5),
}

# ------ Code
dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artista(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia), 'minutos')