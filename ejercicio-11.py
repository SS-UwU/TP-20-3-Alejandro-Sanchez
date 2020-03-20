dinero = float(input("Cantidad a invertir? "))
interes = float(input("Interés porcentual anual? "))
años = int(input("¿Años?"))
a= dinero * (interes / 100 + 1) ** años
print("Capital final: ",a)