#Ejercicio 1 Post-Clase
#Desarrollar las funciones:

def Prod_mas_ingresos(itemes, productos):
    #num_boleta, id_producto, cantidad -> Itemenes
    lista = []
    n = len(productos)
    for _, id_prod, cant_prod in itemes:
        i = 0
        while i < n:
            if id_prod in productos[i]:
                lista.append((productos[i][1],cant_prod*productos[i][2]))
            i += 1
    lista_nom = []
    lista_vent = []
    for prod, venta in lista:
        if prod in lista_nom:
            i = lista_nom.index(prod)
            lista_vent[i] += venta
        else:
            lista_nom.append(prod)
            lista_vent.append(venta)
    m = max(lista_vent)
    k = lista_vent.index(m)
    return lista_nom[k]

def cliente_que_mas_pago(itemes, productos, clientes, ventas):
    #generar lista de venta por boleta
    cant_boletas = ventas[-1][0] #cant de boletas
    n_prod = len(productos)
    i = 1
    lista = []  #lista de boleta, valor compra
    #ciclo de boletas
    while i <= cant_boletas:
        suma = 0
        #sumas compras a la boleta
        for num_boleta, id_prod, cant in itemes:
            if i == num_boleta:
                j = 0
                while j < n_prod:
                    if id_prod in productos[j]:
                        suma += cant*productos[j][2]
                    j += 1
        lista.append((i, suma))
        i += 1

    lista_clientes = [] #valor, nombre
    i = 0
    while i < cant_boletas:
        lista_clientes.append((lista[i][1], ventas[i][2]))
        i += 1
    lista = []
    for rut, nombre in clientes:
        suma = 0
        for valor, rut_cliente in lista_clientes:
            if rut == rut_cliente:
                suma += valor
        lista.append((suma, nombre))
    mayor = 0
    pos = 0
    for valor,name in lista:
        if valor > mayor:
            mayor = valor
            nombre = name
    return nombre

def ingreso_total_por_ventas(itemes, productos):
    n = len(productos)
    total = 0
    for _, id_prod, cant_prod in itemes:
        i = 0
        while i < n:
            if id_prod in productos[i]:
                total += cant_prod*productos[i][2]
            i += 1
    return total

def total_ventas_del_mes(anio, mes, itemes, product, ventas):
    list_boletas = []
    #encontrar boletas del mes
    for num_boleta, fecha, _ in ventas:
        if anio == fecha[0] and mes == fecha[1]:
            list_boletas.append(num_boleta)
    #encontrar items vendidos
    list_item = []
    for num_boleta, id_prod, cant in itemes:
        if num_boleta in list_boletas:
            list_item.append((id_prod, cant))
    #sumar ventas de items
    total = 0
    n = len(product)
    for id_prod, cant in list_item:
        i = 0
        while i < n:
            if id_prod in product[i]:
                total += cant*product[i][2]
            i += 1
    return total

def fecha_ultima_venta_producto(prod, itemes, ventas):
    #encontrar ultima boleta del producto x
    for num_boleta, id_prod, _ in itemes:
        if id_prod == prod:
            boleta = num_boleta
    #encontrar fecha del num de boleta
    for num_boleta, fecha, _ in ventas:
        if boleta == num_boleta:
            date = fecha
    return date

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
    (41235, 'Besos', 3099, 48),
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


a = Prod_mas_ingresos(itemes, productos)
print(a)
b = cliente_que_mas_pago(itemes, productos, clientes, ventas)
print(b)
c = ingreso_total_por_ventas(itemes, productos)
print(c)
d = total_ventas_del_mes(2010, 10, itemes, productos, ventas)
print(d)
e = fecha_ultima_venta_producto(47470, itemes, ventas)
print(e)