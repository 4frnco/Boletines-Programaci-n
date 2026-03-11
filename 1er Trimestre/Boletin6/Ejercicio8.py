###### ejercicio 8 #####
"""
Ejercicio 8: Almacenar precios en una
lista y
mostrar el menor y el mayor precio
"""

prezos = [50, 75, 46, 22, 80, 65, 8]
menor = prezos[0]
mayor = prezos[0]

for prezo in prezos:
    if prezo < menor:
        menor = prezo
    if prezo > mayor:
        mayor = prezo

print("Menor prezo:", menor)
print("Maior prezo:", mayor)