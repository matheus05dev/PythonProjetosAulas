from tkinter import *

def calcular():
    nota1 = float(Entry_nota1.get())
    nota2 = float(Entry_nota2.get())
    nota3 = float(Entry_nota3.get())
    instrumentos = 3
    media = round((nota1 + nota2 + nota3) / instrumentos, 2)

    materia = str(Entry_materia.get())

    label_media.config(text=f"Sua nota média em {materia} foi de {media}")

    if media > 7:
        label_resultado.config(text=f"Parabéns! Você foi aprovado nota acima da média! Parabéns pela sua nota de {media}.")
    elif media == 7:
        label_resultado.config(text=f"Aprovado na média! Mas pode melhorar.")
    else:
        label_resultado.config(text=f"Reprovado. Sua média foi {media}. Vamos se esforçar mais na proxima?")

statusAprovadoAcimaMedia= "Parabéns você foi aprovado tirando uma nota acima da média"
statusReprovado = "Meus pesâmes você foi reprovado por não te tirado a nota média"
statusAprovadoMedia = "Parabéns você foi aprovado com a nota média, bora melhorar e virar um aluno acima da média"

tela = Tk() 
tela.title("Calculadora de Média") 
tela.geometry("1000x800")

lable_materia = Label(tela, text ="Insira o nome da matéria: ", font ="Arial 10 bold italic", justify="left")
lable_materia.grid(column=0,row=0,sticky="w")
Entry_materia=Entry(tela, justify="center", width=20, font="Arial 10 italic") 
Entry_materia.grid (column=1, row=0, pady=(0,20))

lable_nota1 = Label(tela, text ="Nota das atividades cotidianas: ", font ="Arial 10 bold italic", justify="left")
lable_nota1.grid(column=0,row=1,sticky="w")
Entry_nota1=Entry(tela, justify="center", width=20, font="Arial 10 italic") 
Entry_nota1.grid (column=1, row=1, pady=(0,20))

lable_nota2 = Label(tela, text ="Nota da avaliação: ", font ="Arial 10 bold italic", justify="left") 
lable_nota2.grid(column=0,row=2,sticky="w")
Entry_nota2=Entry(tela, justify="center", width=20, font="Arial 10 italic") 
Entry_nota2.grid (column=1, row=2, pady=(0,20))

lable_nota3 = Label(tela, text="Nota do trabalho: ", font ="Arial 10 bold italic", justify="left") 
lable_nota3.grid(column=0,row=3,sticky="w")
Entry_nota3=Entry(tela, justify="center", width=20, font="Arial 10 italic") 
Entry_nota3.grid (column=1, row=3, pady=(0,20))

Botao_calcular = Button(tela, justify="center", text="Calcular", font="Arial 10 bold", bg="black", fg="white",width=30, overrelief="ridge", command=calcular)
Botao_calcular.grid(column=0, row=5, sticky="w")

label_media = Label(tela,text="Média:", font="Arial 10 bold")
label_media.grid(column=0, row=6, pady=(0,20))

label_resultado = Label(tela,text="Status de aprovação:", font="Arial 10 bold")
label_resultado.grid(column=0, row=7, pady=(0,20))

tela.mainloop()