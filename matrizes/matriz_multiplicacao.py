import numpy as np

A = np.array([[1, 3, 2],
              [4, 7, 6]])

B = np.array([[2, 8],
              [3, 1],
              [5, 9]])

linhaA = len(A)
colunaA = len(A[0])
linhaB = len(B)
colunaB = len(B[0])
resultado = [[0 for _ in range(colunaB)] for _ in range(linhaA)]

def multiplica(matriza, matrizb):
    for i in range(linhaA):
        for j in range(colunaB):
            soma = 0
            for k in range(colunaA):
                soma += matriza[i][k] * matrizb[k][j] 
            resultado[i][j] = soma
    return np.array(resultado) 

result = multiplica(A, B)
print(result)