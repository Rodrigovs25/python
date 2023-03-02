primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
print('Digite umas da opções para seguir')
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
while True:
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(primeiro, segundo, primeiro + segundo))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(primeiro, segundo, primeiro * segundo))
    elif opcao == 3:
        print('O maior número entre {} e {} é {}'.format(primeiro, segundo, max(primeiro, segundo)))
    elif opcao == 4:
        primeiro = int(input('Primeiro número: '))
        segundo = int(input('Segundo número: '))
    elif opcao == 5:
        print('Programa encerrado')
        break
    else:
        print('Opção inválida')

"""    
n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))
menu = 0
while menu != 5:
    print('escolha uma opção no menu')
    menu = int(input(('''
    1: para soma
    2: para multiplicar
    3: para ver qual e o maior
    4: para escolher novos numeros
    5: para sair do programa
    digite aqui: ''')))
    if menu == 1:
        soma = n1 + n2
        print('a soma entre {} e {} e de {}'.format(n1, n2, soma))
    if menu == 2:
        multi = n1 * n2
        print('o numero {} multiplicado por {} e {}'.format(n1, n2, multi))
    if menu == 3:
        if n1 > n2:
            print('o numero {} e o maior'.format(n1))
        if n2 > n1:
            print('o numero {} e maior'.format(n2))
    if menu == 4:
        n1 = int(input('digite um novo numero'))
        n2 = int(input('digite mais um novo numero'))
    elif menu == 5:
        print('programa filalizado')
    else:
        print('opção invalida')
print('fim do programa')
"""