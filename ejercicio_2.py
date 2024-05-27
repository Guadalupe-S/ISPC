"""Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared."""
#ingreso de datos 
print('Ingrese las medidas de la habitacion')
largo = int(input('Largo: '))
ancho = int(input('Ancho: '))
precio = int(input('Ingrese el precio por metro cuadrado: '))

#Calculos
metros = largo * ancho
total = metros * precio

#Muestra de valores
print('El costo de mano de obra es: ', total)