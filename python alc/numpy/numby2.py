import numpy as np
np.random.seed(0)

a1 = np.random.randint(10, size=6)
a2 = np.random.randint(10, size=(3, 4))
a3 = np.random.randint(10, size=(3, 4, 5))

print("a3 n° de dimensoes: ", a3.ndim)
print("a3 a tupla inserida no size: ", a3.shape)
print("a3 n° de elementos do vetor: ", a3.size)

len(a3) # tamanho da primeira dimensao

print(a2[0,0])
a2[0, 0] = 12
print(a2[0,0])

#slicing arrays
#a[start:stop;step]

a4 = np.arange(10)
print(a4[-5:]) #imprime os cincos ultimos
print(a4[::-1]) #inverte os elementos de array
print(a4[5::-2])

print(a2[:2,:3]) # duas linhas, tres colunas
print(a2[::-1, ::-1]) # inverte as linhas  e colunas
print(a2[:, 0]) # primeira coluna
print(a2[0, :]) # primeira linha

a2_sub = a2[:2, :2]
print(a2_sub)

a2_sub[0, 0] = 99
print(a2_sub)
print(a2) #modifica o array original, a copia

a2_sub_copy = a2[:2, :2].copy() # criar uma copia do array
print(a2_sub_copy)
a2_sub_copy[0, 0] = 42
print(a2_sub_copy)
print(a2)


# reshaping arrays
grid = np.arange(1, 10).reshape(3, 3) #arrangr: vai uma linha de 9 numeros, reshape: vai formatar o array inicial
print(grid)

#np.newaxis # refazer array

#juntar ou quebrar array

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(np.concatenate([a, b])) # juntar array

grid1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(np.concatenate([grid1, grid1]))
print(np.concatenate([grid1, grid1], axis=1))

#splitting array

oi = [1, 2, 3, 99, 99, 3, 2, 1]
oi1, oi2, oi3 = np.split(oi, [3, 5])
print(oi1, oi2, oi3)

#fancy indexing

rand = np.random.RandomState(42)
arr = rand.randint(100, size=10)
print(arr)
[arr[3], arr[7], arr[2]]
ind = [3, 7, 4]
print(arr[ind])
arr2 = np.arange(12).reshape((3, 4))
print(arr2)
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print(arr2[row, col])
print(arr2[row,:][:, col])
print(arr2[1:, (2, 0, 1)]) # na primeira linha imprime os elementos desejados

mask = np.array([1, 0, 1, 0], dtype=bool)
print(mask)
print(arr2[:, mask]) # retornar as colunas 0 e 2

ind1 = np.arange(10)
arr3 = np.array([2, 1, 8, 4])
print(ind1)
ind1[arr3] = 99
print(ind1)
ind1[arr3] -= 10
print(ind1)

#EVITAR UTILIZAR ELEMENTOS REPETIDOS EM FANCY
#sorting arrays

a4 = np.array([2,1, 4, 3, 5])
print(np.sort(a4)) #ordena os elementos do vetor, criar uma copia do array
print(np.argsort(a4)) #ordena o vetor de acordo com a posicao do elemento

rand1 = np.random.RandomState(42)
arr4 = rand1.randint(0, 10, (4, 6))
print(arr4)
print(np.sort(arr4)) # ordena aws linhas
print(np.sort(arr4, axis=0)) # ordena as colunas, indica sobre dimensao há a interaçao, axis=1 --> vai ordenar as linhas

#partial sorting
arr5 = np.array([7, 2, 3, 1, 6, 5, 4])
print(np.partition(arr5, 3))

#Universal function(ufun)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0/values[i]
    return output
values = np.random.randint(1, 10, size=5)
print(values)
print(compute_reciprocals(values)) #demora muito, tem de vetorizar o codigo
#!timeit (1.0/big_array) --> utilizar menos tempo

#np.absolute(a) = retorna os valores absolutos

#scipy --> biblioteca que contem putras funcoes

mylist = np.random.randint(100)
print(np.sum(mylist)) # realizada mais rapida que a funcao sum do proprio python

nd = np.random.random((3,4))
print(nd)
print(nd.sum())
print(nd.sum(axis=0)) # coluna 0
print(nd.min(axis=1)) # minimo da linhas

#broadcasting
m = np.random.random((3,3))
v = np.array([[10,20,30]]) # linha
print(m+v)
print(m+v.T) #.T--> dar a trasnporta, o vetor virou uma coluna


