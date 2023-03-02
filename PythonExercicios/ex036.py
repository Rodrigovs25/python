casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financi = float(input('Quantos anos de finaciamento? '))
prestaçao = casa/(12*financi)
novo = salario*0.3
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa, financi), end='')
print(' a prestação será de R${:.2f}'.format(prestaçao))
if novo >= prestaçao:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo não pode ser concedido')



