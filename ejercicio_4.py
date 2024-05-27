"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
La promoción de jubilados es sumarle un 10% de descuento
(si posee otros descuentos, se suma los descuentos). 
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

"""
#ingreso de datos
unidades = int(input("Cantidad de leches vendidas vendidas: "))
jubilacion = int(input('El cliente es jubilado(0 = Si y 1 = No): '))

#calculo
precio_final = 0
if unidades >= 12 and unidades <= 24:
    precio_final = (unidades * 1000) * 0.90
elif unidades > 24:
    precio_final = (unidades * 1000) * 0.85
else:
    precio_final = unidades * 1000
#jubilacion
if jubilacion == 0:
    precio_final = precio_final - (precio_final * 0.10)

print('El total es de: ',precio_final)