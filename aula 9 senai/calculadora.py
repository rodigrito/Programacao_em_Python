def calculadora():
    #variaveis locais
    print("Calculadora Python")
    n1 = float(input("nº>> "))
    op = input("+, -, *, /")

    if op == "+":
        n2 = float(input("nº>> "))
        print ("= n1 + n2")

    elif op == "-":
        n2 = float(input("nº>> "))
        print ("= n1 - n2")

    elif op == "*":
        n2 = float(input("nº>> "))
        print ("= n1 * n2")

    elif op == "/":
        n2 = float(input("nº>> "))
        print ("= n1 / n2")
    else:
        print("Digite algo válido")

        
calculadora()
