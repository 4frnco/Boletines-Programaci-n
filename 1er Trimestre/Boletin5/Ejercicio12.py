###### ejercicio 12 #####
"""
Codificar un programa que lea el sueldo de cada uno de los trabajadores de una empresa y
obtenga el número de ellos que ganan entre 1000 y 1750 €, ambos incluídos y, el
porcentaje de trabajadores que ganan menos de 1000 €. Teniendo en cuenta que no se
conoce con antelación el número de trabajadores de la empresa y no se admiten los
sueldos negativos (utiliza como condición de fin un sueldo 0).
"""
entre_1000_1750 = 0
menos_1000 = 0
total_trabajadores = 0

while True:
    sueldo = float(input("Introduce el sueldo (0 para terminar): "))
    if sueldo == 0:
        break
    if sueldo < 0:
        print("No se admiten sueldos negativos.")
        continue

    total_trabajadores += 1
    if 1000 <= sueldo <= 1750:
        entre_1000_1750 += 1
    elif sueldo < 1000:
        menos_1000 += 1

if total_trabajadores > 0:
    porcentaje_menos_1000 = (menos_1000 / total_trabajadores) * 100
    print("Trabajadores entre 1000 y 1750 €:", entre_1000_1750)
    print("Porcentaje con menos de 1000 €:", porcentaje_menos_1000, "%")
else:
    print("No se introdujeron sueldos válidos.")