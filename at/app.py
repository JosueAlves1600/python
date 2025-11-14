import random 

print("Tente adivinhar o numero entre 1 e 100")

numero_secreto = random.randint(1,100)
tentativa = 0
conseguiu = False

while not conseguiu:
    palpite = int(input("Faça sua tentativa: "))
    tentativa +=1

    if palpite > numero_secreto:
       print(f"O Palpite é maior que o número, tente um número menor!") 

    elif palpite < numero_secreto:
       print("O Palpite é menor que o número, tente um número maior!")
    else:
      print(f"Voce acertou em {tentativa} tentativas")