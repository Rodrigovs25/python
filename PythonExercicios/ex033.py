"""
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
numero = [num1, num2, num3]
print('O maior valor digitado foi {}'.format(max(numero)))
print('O menor valor digitado foi {}'.format(min(numero)))
"""
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor valor é {}'.format(menor))
# Verificando quem é o menor
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3
print('O maior valor é {}'.format(maior))
