# Ejercicio 3
#Cree un módulo llamado “mimodulo.py” y agregue la función invertir_digitos(n) que reciba un número entero n,
# y entregue como resultado el número n, con los dígitos en orden inverso.
def invertir_digitos(num):
    return num[::-1]

# ----
num = input("Ingresar numero: ")
print("El valor ingresado es: ", num)
num2 = invertir_digitos(num)
print("El valor invertido es: ", num2)