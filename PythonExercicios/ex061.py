print('=='*10)
print('10 TERMOS DE UMA PA')
print('=='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
an = primeiro
c = 1
while c <= 10:
    print('{} -> '.format(an), end='')
    an += razao
    c += 1
print('FIM')
