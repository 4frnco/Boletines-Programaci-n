###### ejercicio 9 #####
"""
Ejercicio 9: Almacenar dos vectores
en listas y mostrar su producto escalar
"""

vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
producto_escalar = 0

for i in range(len(vector1)):
    producto_escalar += vector1[i] * vector2[i]

print("Producto escalar:", producto_escalar)