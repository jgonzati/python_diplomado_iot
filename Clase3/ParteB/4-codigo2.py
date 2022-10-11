#Ejercicio 4

def codigo_HH(codigo):
    HH = 0
    MM = 0
    HH_state = True
    for d in codigo:
        if HH_state and d != ':':
            HH += int(d)
        elif not HH_state and d != ':':
            MM += int(d)
        else:
            HH_state = False
        codigo = str(HH%24)+':'+str(MM%60)
    return codigo

#---
print(codigo_HH("776199:68556"))