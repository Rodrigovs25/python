#from math import factorial
#n = int(input('Digite um valor para ver o seu fatorial: '))
#print('O fatorial de {} é: {}'.format(n, factorial(n)))
''' COMO FAZER EXPONENCIAL
n = int(input('Digite um valor para ver o seu fatorial: '))
fatorial = n
for c in range(1, n):
    fatorial*=n
print(fatorial)
'''

n = int(input('Digite um valor para ver o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

''' USANDO O FOR
n = int(input('Digite um numero para calcular seu fatorial: '))

c = 0
f = 1
for c in range (1, n):
    f *= n
    n -= 1
print('Seu fatorial é {}.'.format(f))
'''
