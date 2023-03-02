import numpy as np

a = np.array([[2, 1, 3], [3, 1, 4], [5, 7, 12]])
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
c = np.array([[3], [1], [2]])
d = a*b
e = a.T + b
f = a*c
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

dados = np.array([[ 0.7, 0.7 ],
                  [ 0.0, 1.0 ],
                  [ -0.7, 0.7 ],
                  [ -1.0, 0.0 ],
                  [ -0.7, -0.7 ],
                  [ 0.0, -1.0 ],
                  [ 0.7, -0.7 ],
                  [ 1.0, 0.0 ]])
print(dados)
print("\n")
x1 = np.array([[[1],[2],[3]], [[4],[5],[6]]])
print(x1)

g = np.array([[3, 6, 9], [5, 10, 15]])
x = np.array([[2], [1], [1]])
print(g)
print(x)
y = np.dot(g, x)
print(y)
print("\n")
print("\n")
print(dados)
print("\n")
print(dados[:, 0])

print("\n")
print("\n")
x = np.arange(4)
xx = x.reshape(4, 1)
y = np.ones(5)
z = np.ones((3, 4))

print(xx)
print(y)
print(xx+y)

print("\n")
print("\n")
a1 = np.array([6, 9])

def unequal_add(a,b):
    if len(a) < len(b):
        c = b.copy()
        c[:len(a)] += a
    else:
        c = a.copy()
        c[:len(b)] += b
    return(c)


print(unequal_add(dados, a1))