from random import randint
computador = randint(0, 10)
jogador = int(input('Digite um número entre 1 e 10? '))
tot = 1
while jogador != computador:
    if jogador > computador:
        print('Ops, tente um número menor')
    elif jogador < computador:
        print('Ops, tente um número maior')
    jogador = int(input('Digite um número entre 1 e 10? '))
    tot += 1
print('Você acertou!!!')
print('Você precisou de {} tentativas'.format(tot))
