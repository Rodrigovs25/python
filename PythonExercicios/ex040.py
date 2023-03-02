n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Tirando {} e {}, a média é {:.2f}'.format(n1, n2, media))
if media < 5.0:
    print('O aluno está reprovado')
elif 7.0 > media >= 5: # media >= 5 and media < 7:
    print('O aluno está de recuperação')
else:
    print('O aluno está aprovado')
