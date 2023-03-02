km = float(input('Qual é a distância da viagem?'))
if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print('A distância perdorrida foi de {}Km e o preço é R${:.2f}'.format(km, preco))


