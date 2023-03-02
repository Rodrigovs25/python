print('=='*10)
print('10 TERMOS DE UMA PA')
print('=='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
an = primeiro
c = 1
f = 0
mais = 10
while mais != 0:
    f += mais
    while c <= f:
        print('{} -> '.format(an), end='')
        an += razao
        c += 1
    mais = int(input('\nDigite quantos termos a mais você quer? '))
print('Foram mostrados {} termos'.format(f))
print('FIM')
