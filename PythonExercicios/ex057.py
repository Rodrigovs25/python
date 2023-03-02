'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite a letra correta!!!')
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('O sexo escolhido foi {}'.format(sexo))
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.Por favor, informe seu sexo novamente: ')).strip().upper()[0]
if sexo == 'M' or sexo == 'm':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('Sexo {} registrado com sucesso'.format(sexo))