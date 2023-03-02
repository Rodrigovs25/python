# def dobro(x):
#    return x * 2
t = [10, 20 ,30 ,40]
m = t
m[2] = 55
map(str, m) #A função map aplica o objeto-função a cada item do segundo argumento. O resultado é a criação de um novo
# objeto-lista, sem modificar o original.
print(m)