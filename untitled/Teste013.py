# break = para o loop
# continue = vai para o próximo loop
# pass = não faz nada
'''
x = 0
while x < 10:
    print('x is currently: ', x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('x == 3')
    else:
        print('Continuing...')
        continue
'''

'''
x = 0
while x < 10:
    print('x is currently: ', x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('x == 3')
        break
    else:
        print('Conrinuing...')
        continue
'''

# while true: # loop infinito
# print('Uh oh infinte loop')

x = 0
while x < 5:
    print('* ' * x)
    x += 1
while x > 0:
    print('* ' * x)
    x -= 1
