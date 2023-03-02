import numpy as np

toi = np.array(['a', 3, 52, 6])
print(toi)

oi = np.array([1, 4, 3, 14], dtype='float32')
print(oi)

matriz = np.array([range(i, i+3) for i in [2, 3, 4]])
print(matriz)

bi = np.zeros(10, dtype=int) # criar uma lista de zeros
print(bi)

b1 = np.ones((3, 5), dtype=int)
print(b1)

bri = np.full((3, 5), 3.14)
print(bri)

print("agora")
ar = np.arange(0, 20, 2)
print(ar)

li = np.linspace(0, 1, 5) #numeros entre 0 e 1 dividos por 5
print(li)

al = np.random.randint(0, 10, (3, 3)) #numeros aleatorios entre 0 e 1 numa matriz 3 por 3
print(al)

ey = np.eye(3) #matriz identidade
print(ey)

em = np.empty(3) # alocar um espaco da memoria para aquele tamanho
print(em)

print("\n")
a = np.array([[1,2,3],[-3,-2,-1]])
print(a)
print("\n")
a = np.random.randint((3,3))
print(a)

