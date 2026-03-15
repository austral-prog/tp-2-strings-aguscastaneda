def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingrese el gasto: "))
    pago = int(input("Ingrese el pago: "))
        
    vuelto = pago - gasto
        
    pesos = int(vuelto)
        
    print(f"Pesos: {pesos}")
        
    centavos = vuelto % pesos
    print(f"Centavos: {centavos}")
