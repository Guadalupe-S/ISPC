"""
4) En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)
"""
#4 diccionario Familia
familia = {}
for i in range(0,4):
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    dni = input('DNI: ')
    email = input('email: ')
    fecha_nacimiento = input('Fecha de nacimiento: ')

    persona = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "email": email,
        "fecha_nacimiento": fecha_nacimiento
    }

    familia[f"Persona {i}"] = persona
print(familia)

    