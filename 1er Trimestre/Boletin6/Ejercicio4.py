###### ejercicio 4 #####
"""
Ejercicio 4: Almacenar asignaturas en una lista,
preguntar las notas y eliminar
las asignaturas aprobadas,
mostrando solo las que hay que repetir
"""

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Língua"]
repetir = []
for asignatura in asignaturas:
    nota = float(input("Que nota sacaches en " + asignatura + "? "))
    if nota < 5:
        repetir.append(asignatura)

print("Asignaturas a repetir:", repetir)