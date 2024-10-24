import math  # adicionar os calculos matemáticos automaticamente


def calcular(expressao):  # calcular vai ser a funcao que determinada opara o usuario
    try:  # para codigos com excessoes
        # Substitui porcentagem por cálculo
        expressao = expressao.replace('%', '/100 *')
        # Avalia a expressão
        # eval - para strings com código multi-linhas devem ser terminadas com pelo menos um caractere de nova linha quando compiladas
        resultado = eval(expressao)
        return resultado
    except Exception as e:  # except - utilizada em conjunto com a instrução try para lidar com excecoes / exception - classe da excecao
        return f"Erro: {e}"


# calculo
def main():  # main - modulo primario
    print("Calculadora")
    print("Suporte: +, -, *, /, ** (potência), sqrt (radiciação), % (porcentagem)")
    print("Digite 'sair' para encerrar.")

    while True:  # while - repetir o processo ate que receba o 'break'
        expressao = input("Digite a expressão: ")
        if expressao.lower() == 'sair':  # lower - transforma variavel toda em minuscula
            break  # encerramento do processo que usa o 'while'
        resultado = calcular(expressao)
        print(f"Resultado: {resultado}")


if __name__ == "__main__":  # modulo pra fazer as instrucoes de forma que priorize tudo dentro do main funcao
    main()