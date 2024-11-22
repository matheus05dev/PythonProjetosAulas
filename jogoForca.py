preenchimento = 3
listapalavras = []

while preenchimento > 0:
    palavra = input("Digite uma palavra: ")  
    listapalavras.append(palavra)  
    preenchimento -= 1  

print("Todas as palavras:", listapalavras)
