# Ejercicio 4

# 1) Escriba la función factorial_reciproco(n), que retorne el valor de 1/n!
# 2) Escriba la función signo(n) que retorne 1 cuando n es par, y -1 cuando n es impar.
# 3) Escriba las funciones seno_aprox(x, m) y coseno_aprox(x, m) que aproximen el seno y
# el coseno de x, usando los primeros m términos de las sumatorias.

def factorial_reciproco(n):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    inv_n = 1 / prod
    return inv_n

def signo(n):
    return (-1)**n

def sen_approx(x,m):
    i = 0
    sen = 0
    while i <= m:
        num = 2*i +1
        sen += signo(i)*factorial_reciproco(num)*(x**num)
        i += 1
    return sen

def con_approx(x,m):
    k = m
    i = 0
    cos = 0
    while i <= k:
        num = 2*i
        cos += signo(i)*factorial_reciproco(num)*(x**num)
        i += 1
    return cos

# ----
x = 1
n = 6
print('Sen(',x,') es:' ,sen_approx(x,n))
print(con_approx(x,n))