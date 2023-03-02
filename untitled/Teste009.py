print('Balanço de contas')
print()
print('Deixe o nome em branco para encerrar')
print()
total = 0
contas = {}
while 1:
    pessoa = str(input('Digite o nome da pessoa: '))
    if not pessoa:
        break
    while 1:
        resp = input('Quanto gastou {}? '.format(pessoa))
        try:
            gasto = float(resp)
            break
        except:
            print('Número inválido')
    contas[pessoa] = gasto
    total += gasto
numpessoas = len(contas)
print()
print('O número de pessoas é: {}'.format(numpessoas))
print('O total de gastos: {}'.format(total))
media = total/numpessoas
print('Gastos por pessoas: {:.2f}'.format(media))
print()
for nome in contas.keys():
    saldo = media - contas[nome]
    print('Saldo de {}: {:.2f}'.format(nome, saldo))
