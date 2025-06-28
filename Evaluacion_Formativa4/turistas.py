# Diccionario con los datos de los turistas
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

# Función para mostrar turistas por país
def turistas_por_pais(pais):
    lista_turistas = []
    for turista in turistas:  # Ahora turista es el ID de cada persona
        datos = turistas[turista]
        if datos[1].lower() == pais.lower():
            lista_turistas.append(datos[0])
    if len(lista_turistas) == 0:
        print("No hay turistas de ese pais")
    else:
        print(lista_turistas)

# Función para calcular porcentaje de turistas por mes
def turistas_por_mes(mes):
    total = 0
    cuenta = 0
    for turista in turistas:
        total += 1
        datos = turistas[turista]
        fecha = datos[2]
        partes = fecha.split("-")
        mes_turista = int(partes[1])
        if mes_turista == mes:
            cuenta += 1
    if cuenta == 0:
        print("No hay turistas en ese mes.")
    else:
        porcentaje = round((cuenta / total) * 100, 1)
        print(f"El número de turistas equivale al {porcentaje} % del total")

# Función para eliminar un turista por nombre
def eliminar_turista():
    nombre = input("Ingrese nombre del turista a eliminar: ")
    encontrado = False
    turista_a_borrar = ""
    for turista in turistas:
        datos = turistas[turista]
        if datos[0].lower() == nombre.lower():
            encontrado = True
            turista_a_borrar = turista
            break
    if encontrado:
        del turistas[turista_a_borrar]
        print("Turista eliminado con exito")
    else:
        print("Turista no encontrado. No se pudo eliminar")
        
while True:
    print("*******MENU PRINCIPAL*******")
    print("1.- Turistas por pais.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir.")
    try:
        opcion = input("Ingrese opción: ")
    except ValueError as error:
        opcion = -1

    if opcion == "1":
        pais = input("Ingrese pais a buscar: ")
        turistas_por_pais(pais)
    elif opcion == "2":
        while True:
            try:
                mes = int(input("Ingrese mes a buscar: "))
                if mes < 1 or mes > 12:
                    print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente")
                else:
                    turistas_por_mes(mes)
                    break
            except:
                print("Debe ingresar un número válido para el mes")
    elif opcion == "3":
        eliminar_turista()
    elif opcion == "4":
        print("Hasta pronto, gracias por tu prefencia")
        break
    else:
        print("Ingrese una opción válida por favor")