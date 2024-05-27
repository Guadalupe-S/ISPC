"""
Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. 
Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
y así hasta 10

5.1 Resuelva este problema utilizando un mientras y de modo que por la salida se emita la tabla tal como se propone.
5.2 Resuelva este problema utilizando un para y de modo que por la salida se emita la tabla tal como se propone.
"""


print('Tabla de multiplicar')
numero = int(input('Ingrese el numero que necesite generar la tabla: '))

#inicializacion
vuelta = 1
while vuelta != 11:
    resultado = numero * vuelta
    print(numero,'x', vuelta, '=', resultado)

    vuelta += 1