"""
Desarrollar un programa secuencial que permita ingresar un precio
calcular el IVA y mostrar el precio final de lista de un producto
Ejemplo: Si un producto vale $100 y el IVA es 21, el precio de lista es $121
"""

precio = int(input('Precio del producto S/IVA: '))

calculo = precio * 1.21

print('Precio del producto con IVA:', calculo)