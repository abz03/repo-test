'''
Programa: Sistema de bibliotecas.
Utilizar la lista de usuarios y personas definidas a continuación.
El programa debe mostrar un menú que permita:
1 - Buscar un usuario por su rut.
    1.1 - Si el usuario existe mostrar un menú para:
        1.1.1 - Realizar un préstamo de un libro, sólo si hay disponibles.
        1.1.2 - Realizar la devolución de un libro
            1.1.2.1 - Si el libro no existe, permitir registrar el libro que trajo la persona.
    1.2  - Si el usuario no existe, permitir registrar al usuario.
2 - Registrar un nuevo usuario.
3 - Registrar un nuevo libro.
4 - Salir

Debe hacer una función para:
1 - Buscar usuarios
2 - Registrar un usuario
3 - Registrar un libro

Debe usar try-except para verificar todos los posibles códigos peligrosos.
Debe usar mensajes amigables y coherentes con un programa pensado para el encargado de la 
biblioteca. Bien escritos y redactados, puede ayudarse de Chat GPT para esto.
'''

# Lista de usuarios registrados, cada uno tiene nombre, apellido, rut y los libros que tiene prestados
usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": [0]},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

# Lista de libros disponibles en la biblioteca
libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]

# Función que busca un usuario por su RUT
def buscar_usuario(rut):
    for usuario in usuarios:  # Recorre la lista de usuarios
        if usuario["rut"] == rut:  # Si el rut coincide
            return usuario  # Devuelve el usuario encontrado
    return None  # Si no se encuentra, retorna None (que no haag nada)

# Función que permite registrar un nuevo usuario en la lista
def registrar_usuario():
    try:
        nombre = input("Nombre del nuevo usuario: ")
        apellido = input("Apellido: ")
        rut = input("RUT: ")
        if buscar_usuario(rut):           # Validar que el usuario no exista ya
            print("Ya existe un usuario con ese RUT.")
            return
        usuarios.append({"nombre": nombre, "apellido": apellido, "rut": rut, "libros": []}) # Agrega al nuevo usuario a la lista con libros vacíos
        print("Usuario registrado correctamente.")
    except:
        print("Error al registrar el usuario.")

# Función que permite agregar un nuevo libro a la lista
def registrar_libro():
    try:
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        paginas = int(input("Cantidad de páginas: "))
        cantidad = int(input("Cantidad disponible: "))
        nuevo_id = libros[-1]["id"] + 1  # Calcula el nuevo ID
        libros.append({
            "id": nuevo_id,                          #Agrega un id en base al ingresado por el usuario
            "titulo": titulo,                        #Agrega un titulo en base al ingresado por el usuario
            "autor": autor,                          #Agrega un autor en base al ingresado por el usuario
            "ISBN": isbn,
            "paginas": paginas,
            "cantidad_disponible": cantidad
        })
        print("Libro agregado correctamente.")
    except:
        print("Error al registrar el libro, vuelva a intentar nuevamente")

# Función que muestra las opciones para un usuario ya identificado
def menu_usuario(usuario):
    while True:
        print(f" Su Usuario es: {usuario['nombre']} {usuario['apellido']}")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Volver al menú principal")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            try:
                print("Lista de libros disponibles:")
                for libro in libros:
                    print(libro["id"], "-", libro["titulo"], "(", libro["cantidad_disponible"], "disponibles)")

                id_libro = int(input("Ingrese el número del libro que quiere prestar: "))
            except:
                id_libro = -1 #Se asigna un valor invalido

                # Buscamos el libro con ese ID
                libro_encontrado = None
                for l in libros:
                    if l["id"] == id_libro:
                        libro_encontrado = l
                        break
                if libro_encontrado and libro_encontrado["cantidad_disponible"] > 0: #Validamos que el libro este disponible y que exista
                    usuario["libros"].append(id_libro)  # Se registra el préstamo
                    libro_encontrado["cantidad_disponible"] -= 1  # Se reduce la cantidad disponible
                    print("Libro prestado con éxito.")
                elif id_libro == -1:
                    print("Ocurrió un error al prestar el libro, intente nuevamente con valores validos")
                else:
                    print("No se encontró el libro o no hay disponibles.")

        elif opcion == "2":
            try:
                if not usuario["libros"]:
                    print("El usuario no tiene libros prestados.")
                else:
                    print("Libros prestados:", usuario["libros"])
                    id_devolver = int(input("Ingrese el número del libro que desea devolver: "))

                    if id_devolver in usuario["libros"]:
                        usuario["libros"].remove(id_devolver)  # Se quita el libro de su lista
                        libro_devuelto = None
                        for l in libros:
                            if l["id"] == id_devolver:
                                l["cantidad_disponible"] += 1  # Se devuelve una unidad
                                libro_devuelto = l
                                break
                        if libro_devuelto:
                            print("Libro devuelto correctamente.")
                        else:
                            print("Ese libro no está registrado en la biblioteca, intente con un valor valido.")
                            registrar = input("¿Desea registrar el libro que está devolviendo? (si/no): ")
                            if registrar.lower() == "si":
                                registrar_libro()
                    else:
                        print("Ese libro no está prestado por el usuario.")
            except:
                print("Error al devolver el libro, verifique los valores ingresados.")

        elif opcion == "3":
            break  # Sale del menú de usuario y comienza el programa nuevamente.
        else:
            print("Opción inválida.")

# Menú principal del programa
while True:
    print("Bienvenido al sistema de Biblioteca")
    print("1. Buscar usuario por RUT")
    print("2. Registrar nuevo usuario")
    print("3. Registrar nuevo libro")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        rut = input("Ingrese el RUT del usuario: ")
        usuario = buscar_usuario(rut)
        if usuario:
            menu_usuario(usuario)
        else:
            print("Usuario no encontrado.")
            agregar = input("¿Desea registrarlo? (s/n): ")
            if agregar.lower() == "s":
                registrar_usuario()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        registrar_libro()
    elif opcion == "4":
        print("Gracias por usar el sistema de biblioteca.")
        break
    else:
        print("Opción no válida. Ingrese un número valido en base")
