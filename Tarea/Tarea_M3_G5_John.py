# -------------------------------------------------------------------
# Trabajo Final Modulo 2
# Paralelo 2, grupo 5
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Librerias
# -------------------------------------------------------------------
import random # libreria para generar numeros aleatorios
import time
# -------------------------------------------------------------------
# Funciones
# -------------------------------------------------------------------
# Genera temperatura inicial del ambiente, numero entero entre 0 y 35
# grados Celcius
# -------------------------------------------------------------------
def temperatura_inicial_ambiente():
    return random.randint(0, 35)

# -------------------------------------------------------------------
# Genera temperatura actual del ambiente, en función de la temperatura
# en el tiempo anterior y el estado de encendido del calefactor
# -------------------------------------------------------------------
def temperatura_actual_ambiente(temp,estado_calefactor):
    if estado_calefactor:
        temp_actual = temp + random.uniform(0.0,2.0)
    else:
        temp_actual = temp - random.uniform(0.0,2.0)
    return temp_actual

# -------------------------------------------------------------------
# Asigna estado de encendido o apagado del calefactor
# -------------------------------------------------------------------

def estado_inicial_calefactor(temp,temperatura_calefactor):
    if temp <= temperatura_calefactor:
        estado_calefactor = True
    else:
        estado_calefactor = False
    return estado_calefactor

# -------------------------------------------------------------------
# Solicita datos al usuario
# -------------------------------------------------------------------
tiempo_total = int(input('Ingrese tiempo maximo (s):'))
tiempo_medicion = int(input('Tiempo medicion (s):'))
temperatura_calefactor = int(input('Ingrese temperatura de calefactor (°C):'))

# -------------------------------------------------------------------
# Formato textos
# -------------------------------------------------------------------
texto_salida='Tiempo: {:3.0f} (s) - Temperatura actual: {:4.1f} (°C) - Estado Calefactor: {:<}'
nombre_archivo = 'log-tempinicial-{}-tempcalefactor_{}-tiempototal_{}-tiempomedicion_{}.csv'


# -------------------------------------------------------------------
# Ciclo de simulación
# -------------------------------------------------------------------
tiempo=0
while tiempo <= tiempo_total:

    # -------------------------------------------------------------------
    # pasos para el tiempo 0 de simulación
    # -------------------------------------------------------------------
    if tiempo==0:
        # -------------------------------------------------------------------
        # temperatura inicial y estado de funcionamiento del calefactor
        # -------------------------------------------------------------------
        temperatura_ambiente = temperatura_inicial_ambiente()
        estado_calefactor = estado_inicial_calefactor(temperatura_ambiente, temperatura_calefactor)
        tiempo = 0  # inicia en tiempo 0 (s)

        # -------------------------------------------------------------------
        # Archivo para guardar resultados de la simulacion
        # -------------------------------------------------------------------
        nombre_archivo = nombre_archivo.format(temperatura_ambiente, temperatura_calefactor, tiempo_total,
                                               tiempo_medicion)
        archivo = open(nombre_archivo, 'w')
    # -------------------------------------------------------------------
    # Genera temperatura del medio ambiente y calefactor
    # -------------------------------------------------------------------
    temperatura_ambiente = temperatura_actual_ambiente(temperatura_ambiente,estado_calefactor)
    estado_calefactor = estado_inicial_calefactor(temperatura_ambiente, temperatura_calefactor)
    # -------------------------------------------------------------------
    # Escritura de variables en pantalla
    # -------------------------------------------------------------------
    print(texto_salida.format(tiempo,temperatura_ambiente,str(estado_calefactor)))
    # -------------------------------------------------------------------
    # Escritura de variables en archivo CSV
    # -------------------------------------------------------------------
    archivo.write(';'.join(map(str,[round(temperatura_ambiente,1),estado_calefactor]))+'\n')
    # -------------------------------------------------------------------
    # Pausa de simulación
    # -------------------------------------------------------------------
    time.sleep(tiempo_medicion)
    tiempo += tiempo_medicion
# -------------------------------------------------------------------
# Cierre de archivo que almacena los datos generados
# -------------------------------------------------------------------
archivo.close()
