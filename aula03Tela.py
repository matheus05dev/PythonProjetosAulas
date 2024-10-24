from tkinter import * # Importação da biblioteca tkinter

def calcular():
    peso=float(Entry_peso.get())
    altura=float(Entry_altura.get())
    imc = peso/(altura*altura)
    Label_imc.configure(text=f"O seu imc foi de {round(imc)}")


tela = Tk() # Criação da janela
tela.title("IMC") # Definindo o título da janela
tela.geometry("300x200") # Definindo o tamanho da janela

Label_peso = Label(tela, text= "Peso(kg): ", font="Arial 20 bold italic", justify="left") # Etiqueta para a entrada de dados
Label_peso.grid (column=0, row=0, sticky="w") # define onde vai aparecer na tela
Entry_peso = Entry(tela, justify="center", width=5, font="Arial 20 italic") # entrada de dados
Entry_peso.grid(column=1, row=0, pady=(0,20)) # define onde vai aparecer na tela

Label_altura = Label(tela, text= "Altura(m): ", font="Arial 20 bold italic", justify="left") # Etiqueta para a entrada de dados
Label_altura.grid (column=0, row=1, sticky="w") # define onde vai aparecer na tela
Entry_altura = Entry(tela, justify="center", width=5, font="Arial 20 italic") # entrada de dados
Entry_altura.grid(column=1, row=1, pady=(0,20)) # define onde vai aparecer na tela

Label_imc=Label(tela, text="IMC", font="Arial 12 bold italic") # etiqueta que saíra o resultado do imc
Label_imc.grid(column=0, row=6, pady=(0,20)) # define onde vai aparecer na tela

Botao_calcular = Button(tela, justify="center", text="Calcular", font="Arial 10 bold", bg="black", fg="white",width=30, overrelief="ridge", command=calcular)
Botao_calcular.grid(column=0, row=4, sticky="w") # define onde vai aparecer na tela

tela.mainloop() # Executando o loop principal
calcular()