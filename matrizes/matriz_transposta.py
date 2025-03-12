import numpy as np

A = np.array([[2, 3, 8],
              [6, 0, 4],
              [1, 5, 7]])

linhaA = len(A)
colunaA = len(A[0])


transposta = np.zeros((colunaA, linhaA))

for i in range(linhaA):
    for j in range(colunaA):
        transposta[j][i] = A[i][j]

print(transposta)