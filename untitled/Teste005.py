
print('Digite valores a serem somados')
print('Digite [0] para parar o programa')
n = float(input('Digite o número: '))
total = n
while n != 0: # while n:
    n = float(input('Digite o número: '))
    total += n
print('A soma é {:.2f}'.format(total))

'''
print('Digite valores a serem somados')
print('Digite [0] para parar o programa')
total = 0
while 1:
    n = float(input('Digite o número: '))
    if n == 0:
        break
    total += n
print('A soma é {}'.format(total))
'''
