velocidade = float(input('Qual é a velocidade do carro em km/h? '))
multa = (velocidade - 80)*7
if velocidade <= 80:
    print('Você não foi multado')
else:
    print('Você estava a {}km/h e a multa tem o valor de R${:.2f}'.format(velocidade, multa))

