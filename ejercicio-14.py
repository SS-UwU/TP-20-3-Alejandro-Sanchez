barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (-descuento)
print("El coste de una barra fresca es ",precio,"€")
print("El descuento sobre una barra no fresca es ",descuento * 100, "%")
print("El coste final a pagar es " ,-coste,  "€")