def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Ingrese la base del rectangulo: "))
    altura = int(input("Ingrese la altura del rectangulo: "))

    area = base * altura
    print(f"Area: {area}")

    perimetro = 2 * (base + altura)
    print(f"Perimetro: {perimetro}")
