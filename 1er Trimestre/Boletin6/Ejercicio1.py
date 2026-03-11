###### ejercicio 1 #####
"""
Ejercicio 1: Almacenar asignaturas
en una lista, preguntar las notas al
usuario y mostrar cada asignatura con su nota

"""
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Língua"]
notas = []
for asignatura in asignaturas:
    nota = input("Que nota sacaches en " + asignatura + "? ")
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " sacaches " + notas[i])