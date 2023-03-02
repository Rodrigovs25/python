from random import randint
from time import sleep
computador = randint(0, 5)  #randint = faz o computador pensar/sortear
jogador = int(input('Em que número eu pensei entre 0 e 5? ')) #jogador tentar adivinhar
sleep(2)
if jogador == computador:
    print('Você acertou')
else:
    print('Você errouuuu o número é {} e você pensou no {}'.format(computador, jogador))
