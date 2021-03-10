DIA_MAX_30 = 30
DIA_MAX_31 = 31
DIA_MAX_FEB = 29

ENERO = 1
FEBRERO = 2
MARZO = 3
ABRIL = 4
MAYO = 5
JUNIO = 6
JULIO = 7
AGOSTO = 8
SEPTIEMBRE = 9
OCTUBRE = 10
NOVIEMBRE = 11
DICIEMBRE = 12


def main():
    print("\t\tBIENVENIDO USUARIO\n")
    print("Ingresa los datos de tu fecha de nacimiento con número enteros, "+
    "para decirte que signo del zodiaco eres.")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))

    if (mes==MARZO and (dia>=21 and dia<=DIA_MAX_31)) or (mes==ABRIL and (dia>=1 and dia<=20)):
        print("\nTu signo del zodiaco es: Aries\n")
    
    elif (mes==ABRIL and (dia>=21 and dia<=DIA_MAX_30)) or (mes==MAYO and (dia>=1 and dia<=21)):
        print("\nTu signo del zodiaco es: Tauro\n")
    
    elif (mes==MAYO and (dia>=22 and dia<=DIA_MAX_31)) or (mes==JUNIO and (dia>=1 and dia<=21)):
        print("\nTu signo del zodiaco es: Géminis\n")
    
    elif (mes==JUNIO and (dia>=22 and dia<=DIA_MAX_30)) or (mes==JULIO and (dia>=1 and dia<=22)):
        print("\nTu signo del zodiaco es: Cáncer\n")

    elif (mes==JULIO and (dia>=23 and dia<=DIA_MAX_31)) or (mes==AGOSTO and (dia>=1 and dia<=23)):
        print("\nTu signo del zodiaco es: Leo\n")

    elif (mes==AGOSTO and(dia>=24 and dia<=DIA_MAX_31))or(mes==SEPTIEMBRE and(dia>=1 and dia<=23)):
        print("\nTu signo del zodiaco es: Virgo\n")
    
    elif (mes==SEPTIEMBRE and(dia>=24 and dia<=DIA_MAX_30))or(mes==OCTUBRE and(dia>=1 and dia<=23)):
        print("\nTu signo del zodiaco es: Libra\n")

    elif (mes==OCTUBRE and(dia>=24 and dia<=DIA_MAX_31))or(mes==NOVIEMBRE and(dia>=1 and dia<=22)):
        print("\nTu signo del zodiaco es: Escorpión\n")

    elif (mes==NOVIEMBRE and(dia>=23 and dia<=DIA_MAX_30))or(mes==DICIEMBRE and
        (dia>=1 and dia<=21)):
        print("\nTu signo del zodiaco es: Sagitario\n")

    elif (mes==DICIEMBRE and(dia>=22 and dia<=DIA_MAX_31))or(mes==ENERO and(dia>=1 and dia<=20)):
        print("\nTu signo del zodiaco es: Capricornio\n")

    elif (mes==ENERO and(dia>=21 and dia<=DIA_MAX_31))or(mes==FEBRERO and(dia>=1 and dia<=18)):
        print("\nTu signo del zodiaco es: Acuario\n")

    elif (mes==FEBRERO and(dia>=19 and dia<=DIA_MAX_FEB))or(mes==MARZO and(dia>=1 and dia<=20)):
        print("\nTu signo del zodiaco es: Piscis\n")

    else:
        print("\nIngresaste datos que estan fuera de rango. dia:", dia, "y mes:", mes, "\n")

main()