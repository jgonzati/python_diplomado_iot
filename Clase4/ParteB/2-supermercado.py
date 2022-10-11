#Ejercicio 2

def prod_mas_caro(productos):
    lista = []
    for _, _, precio,_  in productos:
        lista.append(precio)
    i = lista.index(max(lista))
    return productos[i][1]

def valor_T_bodega(productos):
    lista = []
    for _, _, precio, cantB in productos:
        lista.append(cantB*precio)
    suma = sum(lista)
    return suma

def ingreso_T_ventas(itemes, productos):
    suma = 0
    n = len(productos)
    print("Productos Comprados:")
    for _, id_prod, cant_prod in itemes:
        i = 0
        while i < n:
            if id_prod in productos[i]:
                suma += cant_prod*productos[i][2]
            i += 1
    return suma

productos = [
    #(id_producto, nombre, precio, cantidad_bodega)
    (41419, 'Fideos', 450, 210),
    (70717, 'Cuaderno', 900, 119),
    (78714, 'Jabon', 730, 708),
    (30877, 'Desodorante', 2190, 79),
    (47470, 'Yogur', 99, 832),
    (50809, 'Palta', 500, 55),
    (75466, 'Galletas', 235, 0),
    (33692, 'Bebida', 700, 20),
    (89148, 'Arroz', 900, 121),
    (66194, 'Lapiz', 120, 900),
    (15982, 'Vuvuzela', 12990, 40),
    (41235, 'Chocolate', 3099, 48),
]

clientes = [
    #(rut, nombre)
    ('11652624-7', 'Juan Perez'),
    ('8830268-0', 'Sebastian Casanueva'),
    ('7547896-8', 'Victor Gamonal'),
]

ventas = [
    #(num_boleta, fecha_venta, rut_cliente)
    (1, (2010, 9, 12), '8830268-0'),
    (2, (2010, 9, 19), '11652624-7'),
    (3, (2010, 9, 30), '7547896-8'),
    (4, (2010, 10, 1), '8830268-0'),
    (5, (2010, 10, 13), '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    #(num_boleta, id_producto, cantidad)
    (1, 89148, 3),
    (2, 50809, 4),
    (2, 33692, 2),
    (2, 47470, 6),
    (3, 30877, 1),
    (4, 89148, 1),
    (4, 75466, 2),
    (5, 89148, 2),
    (5, 47470, 10),
    (6, 41419, 2),
]

print(prod_mas_caro(productos))
print(valor_T_bodega(productos))
print(ingreso_T_ventas(itemes, productos))