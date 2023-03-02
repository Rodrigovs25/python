# + - * / // ** %
# and or not

tax = 11.3/100
price = 19.95
price = price*tax
print(price)
#price + _
price = price + 19.95
print(price)
price = round(price, 2)
print(price)

print('C:\some\name')
print(r'C:\some\name') #caractere de escape: o contrabarra n vai ser interpretado

#string--> n mutável
word = 'python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[4:])
#word[0] = 'j' #vai dar erro
print('j' + word[1:])

s = 'kngjgklmb'
print(len(s))

#lista --> mutavel

square = [1, 4, 9, 17, 25]
square[3] = 16
print(square[3])
print(square[1])
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = [] #tirar o conteudo
print(letters)

a = ['a', 'b', 'c', 'd']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][2])
print(x[1][2])

beathes = ['john', 'paul']
beathes.append('george')
print(beathes)
beathes2 = ['john', 'paul', 'george']
beathes2.append(['stuart', 'pete'])
print(beathes2)
beathes.extend(['stuart', 'pete']) #para mais de um item deve ser usado essa funcao
print(beathes)
print(beathes + ['stuart', 'pete'])
print(beathes.index('george')) #posicao do termo
print(beathes.count('john')) #quantos vezes o termo aparece
beathes.remove('stuart')
print(beathes)
beathes.insert(1, 'ringo') 
print(beathes)
beathes.reverse()
print(beathes)
beathes.sort() #ordena os elementos
print(beathes)

#tuplas --> imutavel

t = (1, 2, 3)
print(t)
l = ['oi', 'peixoto', 'cavalinho']
l = tuple(l) # converte um lista para uma tupla
print(l)
l = list(l) # faz o contrario
print(l)

tup = ('a', 'b', 'c')
print('b' in tup)

#dicionarios

capitals = {'france' : ('Paris', 2140526), 'portugal' : ('lisboa', 1234567)}
capitals['nigeria'] = ('lagos', 6048430)
print(capitals)
print(capitals['france'])
print(len(capitals))
#capitals.popitem() #remove uma chave aleatorio
del capitals['portugal'] #remove a chave
print(capitals)

#controle de fluxo

y = 6
if (y % 2 == 0):
    print('Par')
elif (y == 1):
    print('1')
else:
    print('Impar')

colors = ['red', 'yellow', 'blue']
for color in colors:
    print(color, end = ' ')

print('\n')

for j in range(5): #range(1) = do 0 ate o final, range(1,2): com dois valores do do inicio ate o final, range(1,2,3): o terceiro e a quantidade de casas que vao pular
    print(j, end = ' ')

print('\n')

comp_colors = ['green', 'purple', 'orange']
for i in range(len(comp_colors)): #in = tem uma funcao diferente
    print(colors[i], comp_colors[i])

print('\n')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print('\n')

a, b = 0, 1

while b < 100:
    print(b, end=' ')
    a, b = b, a+b

#funcao


def fib(n): # argumentos
    p, w = 0, 1
    while p<n:
        print(p, end=', ')
        p, w = w, p+w

print('\n')

fib(100)

#def is_odd(n):
#    return n % 2 != 0

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(list(filter(is_odd, num)) #lambda n: n%2 != 0

#lista automatica

print("\n")
numbers = [x for x in range(1, 11)]
print(numbers)

odd_squares = [x*x for x in range(1,11) if x % 2 != 0]
print(odd_squares)

impar_cubos = [x*x*x for x in range(1, 20) if(x*x*x <= 2197)]
print(impar_cubos)

"""
import math
math.factorial(5)

from math import factorial
fatorial(5)

"""