def kadane_algorithm(arr):
    # Inicializa as variáveis com o primeiro elemento do array
    max_atual = max_global = arr[0]

    # Itera sobre o array a partir do segundo elemento
    for num in arr[1:]:
        # Calcula o máximo entre o número atual e a soma do número atual com a soma máxima até o momento
        max_atual = max(num, max_atual + num)
        # Atualiza o máximo global se o máximo atual for maior
        if max_atual > max_global:
            max_global = max_atual

    return max_global

# Exemplo de uso
array = [-1, 9, 8, 1, 1, 7, 6, -10, 1]
soma_maxima = kadane_algorithm(array)
print(f"A soma: {soma_maxima}")
