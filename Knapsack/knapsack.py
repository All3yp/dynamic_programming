## Pseudocode:

# Função Mochila0_1(itens, capacidade):
#     n = comprimento(itens)  # Número de itens
#     matriz = criar_matriz(n + 1, capacidade + 1)  # Criar uma matriz (tabela) para armazenar os resultados
    
#     # Preencha a tabela de programação dinâmica
#     Para i de 0 a n:
#         Para w de 0 a capacidade:
#             Se i == 0 ou w == 0:
#                 matriz[i][w] = 0  # Inicializar a primeira linha e coluna com 0
#             Senão, se pesos[i-1] <= w:
#                 # Se o peso do item atual for menor ou igual à capacidade atual,
#                 # escolher o máximo entre incluir ou não incluir o item na mochila
#                 matriz[i][w] = max(valores[i-1] + matriz[i-1][w-pesos[i-1]], matriz[i-1][w])
#             Senão:
#                 # Se o peso do item atual for maior que a capacidade atual,
#                 # não é possível incluí-lo, então o valor é o mesmo do item anterior
#                 matriz[i][w] = matriz[i-1][w]
    
#     # O valor máximo estará na célula matriz[n][capacidade]
#     retorno matriz[n][capacidade]

def knapsack_0_1(values, weights, capacity):
    n = len(values)
    # Crie uma matriz para armazenar os resultados dos subproblemas
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    # Preencha a matriz usando a abordagem de programação dinâmica
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
    #         # Verifique se o peso do item atual é menor ou igual à capacidade
            if weights[i - 1] <= w:
    #             # Escolha o máximo entre incluir o item ou não
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
    #             # Se o peso do item atual for maior que a capacidade, não o inclua
                dp[i][w] = dp[i - 1][w]

    # O valor máximo estará na célula dp[n][capacity]
    return dp[n][capacity]

# Exemplo de uso
values = [60, 100, 120]  # Valores dos itens
weights = [10, 20, 30]   # Pesos dos itens
capacity = 50            # Capacidade da mochila

resultado = knapsack_0_1(values, weights, capacity)
print("Valor máximo que pode ser colocado na mochila:", resultado) # 220
