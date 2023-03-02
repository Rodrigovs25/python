print('Digite valores a serem somados')
print('Digite [ENTER] para parar o programa')
total = 0
while 1:
    try:
        linha = input('Digite: ')
        n = float(linha)
        total += n
    except:
        if len(linha) == 0:
            break
        elif ',' in linha:
            print('Use o . como separador decimal')
        else:
            print('Isso não parece um número válido.')
print('A soma é {}'.format(total))