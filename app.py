legal = input("digite um numero") ##tipo string
legal = int(input("digite um numero"))##tipo inteiro
legal = float(input("digite um numero"))##duas casas decimais

print("aqui voce mostra na tela")##apenas print
print(f"aqui voce mostra na tela com variavel {legal}")##boa pratica
print("aqui voce mostra na tela com variavel" + legal)## ñ recomendo


import tkinter as tk

janela = tk.Tk()
janela.title("minha janela")
janela.geometry("300x200")
botao=tk.Button(janela, text='clique aqui')
botao.pack("pady=50")
janela.mainloop()