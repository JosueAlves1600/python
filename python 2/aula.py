while True:
    nome = input("Digite seu nome: ")
    nota1 = float(input("Digite sua nota 1: "))
    nota2 = float(input("Digite sua nota 2: "))

 
    media = (nota1 + nota2) / 2
 
    print(f"{nome} sua media é {media}")
 
 
    continuar = input("Quer calcular novamente (s/n)").lower()
 
  
    if continuar !='s':
        print("Saindo...")
        break