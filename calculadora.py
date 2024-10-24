# calculadora
resultado = 0.00

def calculadora():

# opções da operação

    print("Escolha uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Exponenciação (^)")

#entrada de dados operação

    operacao = input("Digite o número da operação (1/2/3/4/5): ")

#entrada de dados dos números

    print("Insira os 2 números para fazer a expressão numérica")
    nument1 = float(input("Insira o primeiro número: "))
    nument2 = float(input("Insira o segundo número: "))

#operações

    if operacao == '1':
        resultado = round(nument1 + nument2)
        print(f"O resultado da soma foi de {resultado}")

    elif operacao == '2':
        resultado = round(nument1 - nument2)
        print(f"O resultado da subtração foi de {resultado}")

    elif operacao == '3':
        resultado = round(nument1 * nument2)
        print(f"O resultado da multiplicação foi de {resultado}")

    elif operacao == '4':
        if nument2 != 0:
            resultado = round(nument1 / nument2)
            print(f"O resultado da divisão foi de {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")

    elif operacao == '5':
        resultado = round(nument1 ** nument2)
        print(f"O resultado da exponenciação foi de {resultado}")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")

calculadora()
