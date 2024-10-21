p1= input ("Escribe la calificacion del parcial 1: ")
p1 = int (p1)
p2 = input ("Escribe la calificacion del parcial 2: ")
p2 = int (p2)
p3 = input ("Escribe la calificacion del parcial 3: ")
p3 = int (p3)
examen = int(input("ingresa el examen: "))
calificacion = p1 + p2 + p3
print("tu calificacion es: ",calificacion)
tf = int(input("ingresa tu trabajo final: "))
calificacionf = calificacion + examen + tf 
print("tu calificacion es: ",calificacionf)