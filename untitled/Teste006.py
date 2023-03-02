print('Digite valores a serem somados')
print('Digite [ENTER] para parar o programa')
total = 0
while 1:
    try:
        n = float(input('Digite o número: '))
        total += n
    except:
        break
print('A soma é {}'.format(total))