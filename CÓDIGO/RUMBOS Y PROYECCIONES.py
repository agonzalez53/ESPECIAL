import math
print("============================================")
print("Programa para calcular rumbos y proyecciones")
print("Realizado por: Alma Judith Gonzalez Montes")
print("============================================")
#Pidiendos datos
x1 = float(input("Ingrese valor de x1: "))
x2 = float(input("Ingrese valor de x2: "))
y1 = float(input("Ingrese valor de y1: "))
y2 = float(input("Ingrese valor de y2: "))
print("=========================================")
print("Realizando  calculo de rumbo y distancia")
print("=========================================")
#calculando rumbo
valor = (x2-x1)/(y2-y1)
rumbo = math.degrees(math.atan(valor))
print ('valor de rumbo -->' + str(rumbo))
#calculando distancia
distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print ('valor de distancia -->' + str(distancia))
print("=========================================")
print("Realizando  calculo de Proyecciones X,Y")
print("=========================================")
#Calculando Proyeccion X,Y
px = distancia*math.sin(rumbo)
py = distancia*math.cos(rumbo)
print ('Proyeccion x -->' + str(px))
print ('Proyeccion y -->' + str(py))
