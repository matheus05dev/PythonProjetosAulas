# Definindo o cardápio
pizzas = ["", "1 - Frango e catupiry", "2 - 4 queijos", "3 - Rúcula com tomate seco", "4 - Atum"]

# Lista para armazenar os pedidos
pedido = []

# Variável de controle para o loop
fecharPedido = "n"

# Loop principal do pedido
while fecharPedido == "n":
    # Exibe o cardápio
    print("\nCardápio:")
    for item in range(1, len(pizzas)):
        print(pizzas[item])
    
    try:
        item = int(input("\nEscolha um item do Cardápio (1-4): "))
    except ValueError:
        print("Por favor, insira um número válido!")
        continue

    if item < 1 or item > 4:
        print("Item não encontrado no cardápio!")
        continue

    print(f"O seu pedido é: {pizzas[item]}")
    pedido.append(pizzas[item])

    if len(pedido) == 4:
        print("\nVocê completou o pedido!")
        break

    # Pergunta se o cliente deseja fechar o pedido
    fecharPedido = input("\nDeseja fechar o pedido? (s/n): ").strip().lower()
    while fecharPedido not in ['s', 'n']:
        fecharPedido = input("Resposta inválida. Deseja fechar o pedido? (s/n): ").strip().lower()

# Exibe o pedido final
print("\nSeu pedido final é:")
for pizza in pedido:
    print(pizza)
