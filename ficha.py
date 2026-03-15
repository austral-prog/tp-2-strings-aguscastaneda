def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input("Ingrese su nombre completo: ")
    email = input("Ingrese su email completo: ")
    nota1 = input("Ingrese su nota1: ")
    nota2 = input("Ingrese su nota2: ")
    nota3 = input("Ingrese su nota3: ")

    encabezado = """
    ========================
        FICHA DEL ALUMNO
    ========================
    """

    print(encabezado)
    print(f"Nombre: {nombre.strip().title()}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre.strip())}")
    print(f"Iniciales: {nombre.strip().title()[0]}{nombre.strip().title()[nombre.strip().title().find(' ') + 1]}")
    print(f"Usuario: {nombre.strip().title()[nombre.strip().title().find(' ') + 1:].lower()}.{nombre.strip().title()[:nombre.strip().title().find(' ')].lower()}")
    print(f"Email valido: {'@' in email}")
    print(f"Dominio: {email.lower()[email.lower().find('@') + 1:]}")
    print(f"Nombre para archivo: {nombre.strip().title().replace(' ', '_')}")
    print(f"Cantidad de a: {nombre.strip().lower().count('a')}")
    print(f"Codigo secreto: {nombre.strip()[::-1].upper()}")
    print(f"Nota 1: {int(nota1)}")
    print(f"Nota 2: {int(nota2)}")
    print(f"Nota 3: {int(nota3)}")
    print(f"Suma: {int(nota1) + int(nota2) + int(nota3)}")
    print(f"Promedio: {(int(nota1) + int(nota2) + int(nota3)) / 3}")
    print(f"Promedio entero: {(int(nota1) + int(nota2) + int(nota3)) // 3}")

    print("=" * 24)
