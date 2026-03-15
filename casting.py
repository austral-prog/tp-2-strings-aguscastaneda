def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input("Ingrese un precio: "))
    descuento = float(input("Ingrese un descuento: "))
    cantidad = int(input("Ingrese un cantidad: "))

    precio_descuento = precio - descuento
    print(f"Precio con descuento: {precio_descuento}")

    total = precio_descuento * cantidad
    print(f"Total: {total}")
 
