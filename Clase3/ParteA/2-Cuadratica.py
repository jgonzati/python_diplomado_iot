#Ejercicio 2
#Escriba un programa que resuelva una ecuación de segundo grado de la forma:
# ax2 + bx + c = 0


def Cuadratica(a, b = 0, c = 0):
    Det = b**2 -4*a*c

    if Det < 0:
        print("No tiene solución real")
        return
    elif Det == 0:
        print("Tiene solución única")
        x = -b/(2*a)
        return x
    else:
        print("Tiene dos soluciones")
        x1 = (-b + Det**.5)/(2*a)
        x2 = (-b - Det**.5)/(2*a)
        return x1, x2

# ----

print(Cuadratica(4, 2, 8))