def calculadora():
    print("==Calculadora Simples==")
    print("Escolha uma Opções")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite uma operação")

    if escolha in ['1','2','3','4']:
        num1 = float(input("Digite o número 1: "))
        num2 = float(input("Digite o número 2: "))

        if escolha == '1':
            resultado = num1 + num2
            print(f"resultado é {resultado}")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"resultado é {resultado}")
        elif escolha =='3':
            resultado = num1 * num2
            print(f"resultado é {resultado}")
        elif escolha == '4':
            resultado = num1 / num2
            print(f"resultado é {resultado}")
    else:
        print("opção invalida. Tente novamente")

calculadora()