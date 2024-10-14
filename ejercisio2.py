"""
Programa 2:
     crear un programa que calcule area y perimetro
     de un rectangulo
     Entradas:
     base: integere
     altura: integere
     Salidas:
     area: integere
     perimetro: integere
     """

base = input("Ingrese la base: ")
base = int(base)
altura = input("Ingresa la altura: ")
altura = int(altura)
area = base * altura
perimetro = (base * altura) * 2
print("El area del rectangulo es", area)
print("El perimetro del rectangulo es", perimetro)
