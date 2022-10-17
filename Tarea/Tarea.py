#Modulo 2
#Tarea Final
#Grupo 5
#16 Oct

import random
import time
#Datos

t_ventana = int(input("Ingresa Ventana de medición en seg: "))
t_muestreo = int(input("Ingresa periodo de muestreo en seg: "))
spT = int(input("Set Point de Tempertatura en [ºC]:  "))
dt = 0  #contador de tiempo
Calefactor = True

#
T_k = random.randint(0, 35) #temperatura actual
print('Temperatura inicial : {} ºC'.format(T_k))
Log = open('log_Tinit_{}_Tcalefactor_{}_tTotal_{}_tMuestreo_{}.csv'.format(T_k,spT,t_ventana,t_muestreo),'w')

while dt < t_ventana:
    deltaT = round(random.uniform(0, 2), 2)  # delta de temp

    if Calefactor:
        T_k += deltaT
    else:
        T_k -= deltaT

    if T_k < spT:
        Calefactor = True
    else:
        Calefactor = False
    print(round(T_k,2), Calefactor)
    dt += t_muestreo
    Log.write('{};{}\n'.format(round(T_k,2),Calefactor))
    time.sleep(t_muestreo)
print('Fin de medición')
Log.close()
