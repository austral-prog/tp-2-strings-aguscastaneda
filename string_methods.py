def string_methods():
    """Demuestra el uso de métodos de string."""
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"

    print(f"Strip: {nombre.strip()}")
    print(f"Lstrip: {nombre.lstrip()}")
    print(f"Rstrip: {nombre.rstrip()}")

    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")

    print(f"Find: {frase.find('gran')}")
    print(f"Replace: {frase.replace('programacion', 'desarrollo')}")
    print(f"Count: {frase.count('a')}")

    print(f"Contiene Python: {'Python' in frase}")
    print(f"Contiene Java: {'Java' in frase}")

    print(f"Slice: {frase[:6]}")
    print(f"Paso: {frase[:6:2]}")
    print(f"Reverso: {frase[:6][::-1]}")

    print(f"Formato: {nombre.strip()} sabe {frase[:6]}")

    print("Linea 1")
    print("Linea 2")
    print("Linea 3")
