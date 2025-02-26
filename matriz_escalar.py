import numpy as np

A = np.array([[2, 3, 8],
              [6, 0, 4],
              [1, 5, 7]])

linhaA = len(A)
colunaA = len(A[0])
escalar = 3
resultado = np.zeros((colunaA, linhaA))

for i in range(linhaA):
    for j in range(colunaA):
        resultado[i][j] = A[i][j] * escalar

print(resultado) 