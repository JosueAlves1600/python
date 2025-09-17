import tkinter as tk

#0 1-amarelo 2-verde
estado = 0
def trocar():
    global estado
    estado = (estado+1)%3
    desenhar()

def desenhar():
    cores=["grey20", "grey20", "grey20"]
    if estado == 1:
       cores[0] = "red"
    elif estado == 2:
        cores[1] = "yellow"
    else: 
        cores[2] = "green"

    canvas.itemconfig(circulo_vermelho, fill=cores[0])
    canvas.itemconfig(circulo_amarelo, fill=cores[1])
    canvas.itemconfig(circulo_verde, fill=cores[2])

##criando a janela
root = tk.Tk()
root.title("Semáforo Fiap")

canvas = tk.Canvas(root, width=120, height=300, bg="black")
canvas.pack(padx=10, pady=10)

##criando os 3 circulos
circulo_vermelho = canvas.create_oval(20, 20, 100,100, fill="grey20")
circulo_amarelo = canvas.create_oval(20, 110, 100,190, fill="grey20")
circulo_verde = canvas.create_oval(20, 200, 100,280, fill="grey20")

##criando um botao
botao = tk.Button(root, text="Trocar cor", command=trocar)
botao.pack(pady=(0,10))

##criando janela
root.mainloop()