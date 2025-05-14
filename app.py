nota1 = float(input("Digite 1 nota 1: "))
nota2 = float(input("Digite a nota 2: ")) #input tipo numerico
nome = input("Digite seu nome: ") #input do tipo string

media = (nota1 + nota2) / 2

if media <= 6:
    print(f"{nome} sua média é: {media}") #tem uma string e variavel
else:
    print(f"{nome} voce esta aprovado {media}")


# def calcular():
  # print("Escolha a operação:")
  # print("1 - Adição")
  # print("2 - Subtração")
  # print("3 - Multiplicação")
  # print("4 - Divisão")
  # escolha = input("Digite a opção (1/2/3/4): ")
  # if escolha in ('1', '2', '3', '4'):
     #  num1 = float(input("Digite o primeiro número: "))
     #  num2 = float(input("Digite o segundo número: "))
     #  if escolha == '1':
       #    resultado = num1 + num2
       #    operacao = '+'
    #   elif escolha == '2':
        #   resultado = num1 - num2
        #   operacao = '-'
    #   elif escolha == '3':
        #   resultado = num1 * num2
        #   operacao = '*'
    #   elif escolha == '4':
        #   if num2 == 0:
            #   print("Erro: divisão por zero.")
            #   return
       #    resultado = num1 / num2
        #   operacao = '/'
    #   print(f"{num1} {operacao} {num2} = {resultado}")
#   else:
    #   print("Opção inválida.")