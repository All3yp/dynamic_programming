def fibonacci(n):
    """
    Calcula o n-ésimo número na sequência de Fibonacci de forma recursiva.

    Args:
        n (int): O índice do número na sequência.

    Returns:
        int: O n-ésimo número na sequência de Fibonacci.
    """
    if n <= 1:
        # Caso base: Retorna n para n igual a 0 ou 1.
        return n
    else:
        # Passo recursivo: Calcula a soma dos dois números anteriores na sequência.
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 9
    print(str(n) + "th Fibonacci Number: " + str(fibonacci(n)))
