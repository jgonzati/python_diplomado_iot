import math

def perimetro (r):
   result = 2*math.pi*r
   return result

radio = int(input("Ingresar Radio: "))

print("El perimetro es :", perimetro(radio))