print("Tabuada do 1 ao 10")
opção = input("Digite o número da tabuada que deseja (1 a 10): ")

if opção in ['1','2','3','4','5','6','7','8','9','10']:
    num = int(opção)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("OPÇÃO ERRADA!")

##numeroDigitado = int(input("Digite um numero: "))

##for i in range(0,10,1):
    ##print(f"{numeroDigitado}")

    