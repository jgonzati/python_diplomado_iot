#Trabajo Personal - Ejercicio 2
#El banco CBI necesita implementar mejoras en sus mecanismos de seguridad, precisamente en los que
# están relacionados con la generación de claves iniciales para sus clientes de tarjetas de crédito.
#Desarrolle un programa que permita generar una clave de 4 dígitos, usando el siguiente algoritmo:
#• Leer tantos números como sea necesario para generar la clave.
#• Para cada número deberá recorrer sus dígitos y encontrar el menor.
#• Si el dígito menor es par, pasará a formar parte de la clave, en caso contrario,
# se procesa el siguiente número hasta formar la clave de 4 dígitos.
#• Mostrar la clave obtenida.

nclave: int = 0  #contador de digitos de clave
menor = 0
last = 0
digito = ''
num = input("Ingresa numeros al azar: ")
largo = len(num)

i = 0
while nclave < 4:
    digito += str(i)
    nclave += 1
    i += 1

print(digito)