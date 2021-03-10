NUM_PI = 3.14159

def calcularAreaCuadrado(lado:float)->float:
    return (lado*lado)

def calcularAreaTriangulo(base:float, altura:float)->float:
    return (base*altura)/2

def calcularAreaCirculo(radio:float)->float:
    return NUM_PI*(radio*radio)


def main():
    print("\t\tBIENVENIDO USUARIO\n\n")
    print("Cálcularemos el área de las siguientes figuras: cuadrado, triangulo y citculo.")
    print("Ingresa el dato del cuadrado.")
    lado = float(input("Lado: "))

    print("\nIngresa los datos del triangulo.")
    base = float(input("Base: "))
    altura = float(input("Altura: "))

    print("\nIngresa el dato del círculo.")
    radio = float(input("Radio: "))

    print("\nÁrea del cuadrado: ", calcularAreaCuadrado(lado))
    print("Área del triángulo: ", calcularAreaTriangulo(base, altura))
    print("Área del círculo: ", calcularAreaCirculo(radio))

main()