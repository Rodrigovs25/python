salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    novo = salario + (salario*1/10)   # salario*1.1
else:
    novo = salario + (salario*3/20)   # salario*1.15
print('Seu novo salário é de R${:.2f}'.format(novo))
