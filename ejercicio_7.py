"""
Actividades parte 1: Iniciando
Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for)
que consideren adecuados para cada uno de estos casos:
1)Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 
2)Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo


"""
#1)pedir nombres y mostrar
list_nombres = []
for i in range(0, 10):
    nombre = input('Ingresar un nombre:')
    if nombre in list_nombres:
        print('Error, no se puede repetir los nombres')
        nombre = input('Ingresar nuevamente un nombre:')
    
    list_nombres.append(nombre)
print('Los nombres ingresados son: ',list_nombres)

#2 Eliminar elementos y ordenar
list_nombres.pop(2)
list_nombres.pop()
list_nombres.sort()
print('lista con elementos eliminados: ', list_nombres)



