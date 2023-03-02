ano = int(input('Ano do nascimento: '))
from datetime import date
hoje = date.today().year
idade = hoje - ano
print('O alteta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: mirim')
elif idade <= 14:
    print('Classificação: infantil')
elif idade <= 19:
    print('Classificação: junior')
elif idade <= 25:
    print('Classificação: sênior')
else:
    print('Classificação: master')
