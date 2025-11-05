###### ejercicio 10 #####
"""
Ejercicio 10: Almacenar dos matrices
en listas anidadas y mostrar su producto
"""

a = [(1, 2, 3), (4, 5, 6)]
b = [(-1, 0), (0, 1), (1, 1)]
resultado = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            resultado[i][j] += a[i][k] * b[k][j]

print("Producto de matrices:")
for fila in resultado:
    print(fila)