###### ejercicio 1 #####
"""
Un almacén clasifica sus productos según la siguiente tabla de
ventas anuales:

Ventas anuales    Artículo de consumo
<= 100            bajo
>100 y <= 500     medio
>500 y <= 1000    alto
>1000             primera necesidad

Conocido el nombre del artículo y las ventas anuales. Indicar de qué tipo es.
"""
nom_articulo = input("Dime el nombre de tu articulo: ")
num_ventas = int(input("Dime el numero de ventas de este articulo: "))

if num_ventas <= 100:
    print("El articulo", nom_articulo, "es de tipo bajo")

elif num_ventas > 100 and num_ventas <= 500:
    print("El articulo", nom_articulo, "es de tipo medio")

elif num_ventas > 500 and num_ventas <= 1000:
    print("El articulo", nom_articulo, "es de tipo alto")

elif num_ventas > 1000:
    print("El articulo", nom_articulo,"es de tipo de primera necesidad")