'''
list(range(0, 10))
r = range(10, 25)
print(tuple(r))  # podemos usar a função tuple para transformar a lista em tupla.
'''

for c in range(1, 51):
    if c % 3 == 0 and c % 5 == 0:
        print('{:2} - FizzBuzz'.format(c))
    elif c % 3 == 0:
        print('{:2} - Fizz'.format(c))
    elif c % 5 == 0:
        print('{:2} - Buzz'.format(c))

