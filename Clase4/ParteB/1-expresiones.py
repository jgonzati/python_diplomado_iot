#Ejercicio 1
#Considere las siguientes expresiones

a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

# ----
print('1.', a < b)
print('2.', y + w)
print('3.', x + a)
print('4.', len(v))
print('5.', v[1][1])
print('6.', c[0])
print('7.', a + b[1:5])
print('8.', (a+b)[1:5])
print('9.', str(a[2]) + str(b[2]))
print('10.', str(a[2] + b[2]))
print('11.', str((a+b)[2]))
print('12.', str(a+b)[2][0])