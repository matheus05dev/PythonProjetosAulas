import random


def criar_lista_palavra():
    palavras = []
    while True:
        palavra = input("Digite uma palavra (ou'sair' para encerrar): ")
        if palavra.lower() == 'sair':
            break
        palavras.append(palavra.lower())
    return palavras


def jogar(palavras):
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ['_' for letra in palavra_secreta]
    tentativas = 5
    while tentativas > 0 and '_' in letras_acertadas:
        print(''.join(letras_acertadas))
        chute = input("Chute uma letra ou palavra da forca: ").lower()

        if chute in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    letras_acertadas[i] = chute
            print("Acertou")
        else:
            tentativas -= 1
            print("Errou, restam ", tentativas, "tentativas")
    if '_' not in letras_acertadas:
        print("Parabéns, você ganhou")
    else:
        print("Você perdeu, a palavra secreta era: ", palavra_secreta)

lista_palavra = criar_lista_palavra()

jogar(lista_palavra)