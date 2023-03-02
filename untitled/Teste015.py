#def greeting(name):
#    greeting('rodrigo')
#    print('Hello {}'.format(name))
'''
def add_num(num1, num2):
    return num1+num2
result = add_num(4, 5)
print(result)
'''
'''
from math import sqrt
def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(sqrt(num))):
        if num % i == 0:
            return False
    return True
is_prime(11)
'''
'''
def obterdominio(s):
    return s.split('@')[-1]
print(obterdominio('myemail@mydomai.com'))
'''

from math import pi
rad = float(input('Digite o raio: '))
def volume(rad):
    return (rad**3) * (4/3) * (pi)
print('O volume é de {:.2f}'.format(volume(rad)))