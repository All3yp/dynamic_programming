def linear_search(elements, value):
    for index, element in enumerate(elements):
        if element == value:
            return index
    return -1

# Exemplo de uso
elements = [1, 3, 5, 7, 9, 11, 13, 15, 17]
value = 11

result = linear_search(elements, value)
if result != -1:
    print(f"O elemento {value} foi encontrado no índice {result}.")
else:
    print(f"O elemento {value} não foi encontrado na lista.")