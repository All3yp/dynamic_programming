def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Índices esquerdo e direito

    while left <= right:
        mid = (left + right) // 2  # Índice do elemento do meio

        if arr[mid] == target:
            return mid  # O elemento foi encontrado, retorna o índice
        elif arr[mid] < target:
            left = mid + 1  # Ajuste o índice esquerdo
        else:
            right = mid - 1  # Ajuste o índice direito

    return -1  # Elemento não encontrado, retorna -1

# Exemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7

resultado = binary_search(arr, target)

if resultado != -1:
    print(f"O elemento {target} foi encontrado no índice {resultado}.")
else:
    print(f"O elemento {target} não foi encontrado na coleção.")


# Exemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7

resultado = binary_search(arr, target)

if resultado != -1:
    print(f"O elemento {target} foi encontrado no índice {resultado}.")
else:
    print(f"O elemento {target} não foi encontrado na coleção.")