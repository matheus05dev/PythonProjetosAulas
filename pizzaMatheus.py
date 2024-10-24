#variavéis
Preco_Pessoas = 0.00
Preco_Total = 0.00
Preco_Pizza = input
Preco_Bebida = input
Numero_Pessoas=input

#declanrando tipo das váriaveis
Preco_Total = float
Preco_Pessoas= float

#entrada de dados
Numero_Pessoa = int(input ("Quantas pessoas tem na festa? "))
Preco_Pizza = float (input("Quantas que foi o preço da(s) pizza(s)? "))
Preco_Bebida = float (input("Quanto que foi preço da(s) bebida(s)? "))

#processo
Preco_Total = round(Preco_Pizza+Preco_Bebida,2)
Preco_Pessoas = round(Preco_Total/Numero_Pessoa,2)

#impressão
print(f"O preço total foi de {Preco_Total}")
print (f"O preço foi de {Preco_Pessoas} por pessoa")
print (f"O preço das bebidas foi de {Preco_Bebida}")
print (f"O preço das pizzas foi de {Preco_Pizza}")