# emite uma mensagem
print("Hello world")
print("Bem-vindo ao Mundo Python") 
# emite mensagem usando separador
print("Hello","World","Bem","Vindo","ao","Mundo","Python", sep=" ") 
print("Hello","World","Bem","Vindo","ao","Mundo","Python", sep="_") 
print("Hello","World","Bem","Vindo","ao","Mundo","Python", sep="*")
print("Hello world") 
# declaração de variável
idade = 16 # declaração de uma variavél número inteiro - INTEGER 
altura = 1.68  # declaração de uma variavél número flutuante - Float 
nome = "Matheus"  # declaração de uma variavél texto  
print("Idade:",idade)
print(f"Idade: {idade}")
print("nome:", nome)
print(f"nome: {nome}")
print("altura:", altura)
print(f"altura: {altura}")
print(nome, "tem a altura de", altura, "em metros e tem", idade, "anos de idade")
print(f"O {nome} tem a altura de {altura} em metros e tem {idade} anos de idade")
#imprimir variavel
print(type(idade))
print(type(nome))
print(type(altura))
print("a variavel idade e do tipo",type(idade),"a variavel nome e do tipo",type(nome),"a variavel altura e do tipo",type(altura))
# Entrada de dados
print ("Ola prazer em te conhecer!")
nome_ent=input("Qual e o seu nome?")
idade_ent=int(input("Qual e a sua idade?"))
altura_ent=float(input("Qual sua altura?"))
print(f"Olá {nome_ent} ! Voce tem {idade_ent} anos e tem {altura_ent} em metros" )
signo_ent=str(input(f"Qual seu signo {nome_ent}?"))
print(f"Que legal {nome_ent}, voce é de {signo_ent}")