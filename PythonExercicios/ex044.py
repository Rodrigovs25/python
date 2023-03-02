print('{:=^40}'.format(' LOJAS PICAS '))
preco = float(input('Qual o preço do produto?R$ '))
condicao = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if condicao == 1:
    novo = preco * 0.9
    print('Sua compra era de R${:.2f} e agora vai custar R${:.2f}.'.format(preco, novo))
elif condicao == 2:
    novo = preco * 0.95
    print('Sua compra era de R${:.2f} e agora vai custar R${:.2f}.'.format(preco, novo))
elif condicao == 3:
    novo = preco / 2
    print('Sua compra é de R${:.2f} com 2 parcelas no valor de R${:.2f}.'.format(preco, novo))
elif condicao == 4:
    quantidade = int(input('Quantas parcelas? '))
    novo = preco * 1.2
    parcela = novo / quantidade
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(quantidade, parcela))
    print('Sua compra de R${:.2f} vai custar R${} no final.'.format(preco, novo))
else:
    print('ERRO')
