frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
#for c in range(len(junto) - 1, -1, -1):
#    inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palídromo')
else:
    print('A frase NÃO é um palídromo')