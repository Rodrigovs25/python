from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
computador = randint(0, 2)
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 13)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogada]))
print('-=' * 13)
"""
if jogada == 0 and computador == 0 or jogada == 1 and computador == 1 or jogada == 2 and computador == 2:
    print('O jogo terminou empatado.')
elif jogada == 0 and computador == 2 or jogada == 1 and computador == 0 or jogada == 2 and computador == 1:
    print('Você venceu o jogo')
elif jogada == 0 and computador == 1 or jogada == 1 and computador == 2 or jogada == 2 and computador == 0:
    print('Você perdeu o jogo')
else:
    print('Você digitou a opção errada')
"""
if computador == 0:
    if jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JODAGA INVÁLIDA')
elif computador == jogada:
    print('EMPATE')
elif computador == 1:
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('JODAGA INVÁLIDA')
elif computador == 2:
    if jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 0:
        print('JOGADOR VENCE')
    else:
        print('JODAGA INVÁLIDA')

