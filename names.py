def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nombre_completo = f"{nombre} {apellido}"
    print(nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print(f"\t{nombre_completo}")


