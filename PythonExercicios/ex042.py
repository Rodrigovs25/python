r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Os segmentos podem formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo é isósceles.')
    else:  # elif r1 != r2 != r3 != r1:
        print('O triângulo é escaleno.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')