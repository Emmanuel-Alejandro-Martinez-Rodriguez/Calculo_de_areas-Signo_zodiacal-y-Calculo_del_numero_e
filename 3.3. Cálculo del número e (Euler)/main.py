def calcaularFactorial(n:int)->int:
    factorial = 0

    if n==0:
        factorial = 1
    
    elif n>0:
        factorial = n*calcaularFactorial(n-1)

    else:
        factorial = -1

    return factorial

def main():
    print("\t\tBIENVENIDO USUARIO\n")
    limite = int(input("Ingresa el número para calcular euler: "))
    
    n = 0
    e = 0
    while n<limite:
        e += 1/calcaularFactorial(n)
        n += 1
        
    print("\nEl resultado es", e)


main()