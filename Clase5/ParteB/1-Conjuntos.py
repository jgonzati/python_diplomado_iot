#Ejercicio 1

a = {5, 2, 3, 9 ,4}
b = {3, 1}
c = {7, 5, 5, 1, 8, 6}
d = [6, 2, 4 ,5, 5 ,3, 1, 3, 7, 8]
e = {(2, 3), (3, 4), (0, 5)}
f = [{2, 3}, {3, 4}, {4, 5}]

# -----
print(len(c))
print((len(set(d))))
print(a&(b|c))
print((a&b)|c)
print(c-a)
print(max(e))
print(f[0]<a)