################ ejercicio 10 ##############
"""
Hacer el algoritmo y programa que calcule el sueldo bruto y líquido, a percibir por una
persona. Para eso hay que tener en cuenta, que el sueldo total incluye los siguientes
conceptos:

- Sueldo fijo.
- Comisión: 5% sobre importe total de ventas
- Kilometraje: 2 € por km
- Dietas: 30 € por día de desplazamiento.

Para calcular el sueldo líquido debemos descontarle al sueldo bruto:

- I.R.P.F. = 18 % del sueldo total.
- Retención a seguridad social: 36 €.
"""
sueldo_fijo = float(input("Introduce el sueldo fijo (€): "))
ventas = float(input("Introduce el importe total de las ventas (€): "))
kilometros = float(input("Introduce los kilómetros recorridos: "))
dias_desplazamiento = int(input("Introduce el número de días de desplazamiento: "))

comision = ventas * 0.05
pago_kilometraje = kilometros * 2
dietas = dias_desplazamiento * 30

sueldo_bruto = sueldo_fijo + comision + pago_kilometraje + dietas
irpf = sueldo_bruto * 0.18
sueldo_liquido = sueldo_bruto - irpf - 36

print("Sueldo bruto: ", round(sueldo_bruto, 2), "€")
print("Sueldo líquido: ", round(sueldo_liquido, 2), "€")