def ficha():
    nombre = input()
    email = input()
    nota1 = input()
    nota2 = input()
    nota3 = input()

    nombre_limpio = nombre.strip().title()
    email_limpio = email.strip().lower()

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_limpio}")

    print(f"Caracteres en nombre: {len(nombre_limpio)}")

    espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[espacio+1]
    print(f"Iniciales: {iniciales}")

    usuario = nombre_limpio[espacio+1:].lower() + "." + nombre_limpio[:espacio].lower()
    print(f"Usuario: {usuario}")

    print(f"Email valido: {'@' in email_limpio}")

    dominio = email_limpio[email_limpio.find("@")+1:]
    print(f"Dominio: {dominio}")

    print(f"Nombre para archivo: {nombre_limpio.replace(' ', '_')}")

    print(f"Cantidad de a: {nombre_limpio.lower().count('a')}")

    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")

    n1 = int(nota1)
    n2 = int(nota2)
    n3 = int(nota3)

    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")

    suma = n1 + n2 + n3
    print(f"Suma: {suma}")

    promedio = suma / 3
    print(f"Promedio: {promedio}")

    print(f"Promedio entero: {suma // 3}")

    print("========================")
