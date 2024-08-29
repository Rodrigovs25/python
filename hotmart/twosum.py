
def encontrar_pares(array, alvo):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == alvo:
                return [array[i], array[j]]
    return []

array = [0, 1]
alvo = 98
resultado = encontrar_pares(array, alvo)
print("Resultado:", resultado)
