import numpy as np

print(np.__version__)

#1-- criar um vetor com elementos dentro da chave
vetor = np.array([1, 10])
print(vetor)

#2-- criar um vetor com n elementod especificados
vetor1 = np.arange(10)
print(vetor1)

#3-- funcao que especifica tudo, full(dimensao da M, o que vai esta, tipo da variavel)
matriz = np.full((3, 3), True, dtype=bool)
#np.ones((3, 3), dtype=bool) --> funcao que preencher tudo de um e odtype modificar para booleno
print(matriz)

#4-- como satifazer certas condicao
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr % 2 == 1]) # so vai imprimir os numeros requisitados

#5-- substituir uns itens por outros
arr2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2[arr2 % 2 == 1] = -1
print(arr2)

#6-- substituir uns itens sem afetar o array original
arr3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr3) # criar uma copia e modifica
print(arr3)
print(out)

#7-- refazer um array
arr4 = np.arange(10)
print(arr4.reshape(2, -1)) # detrmi

#8-- como juntar dois arrays verticamente
a1 = np.arange(10).reshape(2, -1)
b1 = np.repeat(1, 10).reshape(2, -1)
print(np.concatenate([a1, b1], axis=0))
#np.vstack([a1, b1])
#np.r_[a1, b1]

#9-- como juntar dois arrays horizontalamente
a2 = np.arange(10).reshape(2, -1)
b2 = np.repeat(1, 10).reshape(2, -1)
print(np.concatenate([a2, b2], axis=1))
#np.hstack([a2, b2])
#np.c_[a2, b2]

#10-- como gerar sequencias personalizadas
arr5 = np.array([1, 2, 3])
print(np.r_[np.repeat(arr5, 3), np.tile(arr5, 3)]) # repeat: vai repetir cada elemento x vezes; tile: vai repetir a sequencia x vezes

#11-- como ver itens comuns entre dois arrays
a3 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b3 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.intersect1d(a3, b3))

#12-- remoção de itens de um array que existem em outro
a4 = np.array([1, 2, 3, 4, 5])
b4 = np.array([5, 6, 7, 8, 9])
print(np.setdiff1d(a4, b4)) # a-b

#13-- obter as posicoes onde os elementos de duas matrizes combinam
a5 = np.array([1,2,3,2,3,4,3,4,5,6])
b5 = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a5 == b5))

#14-- como extrair os numeros de um intervalo de uma matriz
arr6 = np.arange(15)
index = np.where((arr6 >= 5) & (arr6 <= 10))
print(arr6[index])
#index = np.where(np.logical_and(a>=5, a<=10))

#15-- escalares para funcionar em matrizes, retorna o maior vetor
def maxx(x, y):
    if x>= y:
        return x
    else:
        return y
pair_max = np.vectorize(maxx, otypes=[float])
a6 = np.array([5, 7, 9, 8, 6, 4, 5])
b6 = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a6, b6))

#16-- como trocar dois colunas em uma matriz
arr7 = np.arange(9).reshape(3, 3)
print(arr7)
print(arr7[:, [1, 0, 2]])

#17-- como trocar duas linhas de uma matriz
arr8 = np.arange(9).reshape(3, 3)
print(arr8)
print(arr8[[1, 0, 2], :])

#18-- inverter as linhas de um array 2d
arr9 = np.arange(9).reshape(3, 3)
print(arr9)
print(arr9[::-1])

#19-- como inverter as colunas de um array 2d
arr10 = np.arange(9).reshape(3, 3)
print(arr10)
print(arr10[:, ::-1])

#20-- uma matriz contendo numeros entre 5 e 10
arr11 = np.arange(9).reshape(3, 3)
rand_arr1 = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
print(rand_arr1)
#np.random.uniform(5, 10, size=(5, 3))

#21-- impressao de ate 3 casas decimais
rand_arr2 = np.random.random([5, 3])
np.set_printoptions(precision=3)
print(rand_arr2[:4])

#22-- como imprimir um array suprimindo a noratao cientifica
np.random.seed(100)
np.set_printoptions(suppress=False)
rand_arr3 = np.random.random([3, 3])/1e3
print(rand_arr2)
np.set_printoptions(suppress=True, precision=6)  # precision is optional
print(rand_arr2)

#23-- limitacao de itens impressos numa matriz
a7 = np.arange(15)
np.set_printoptions(threshold=6)
print(a7)

#24-- imprimir a matriz sem truncar
np.set_printoptions(suppress=False)
a8 = np.arange(15)
np.set_printoptions(threshold=np.nan)
print(a8)




