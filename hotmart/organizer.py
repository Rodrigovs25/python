def reorganizar_lista(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares + impares

lista = [41, -17, 54, 75]
resultado = reorganizar_lista(lista)
print(resultado)
