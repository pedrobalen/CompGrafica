import numpy as np

A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])


eh_identidade = True

for i in range(len(A)):
    for j in range(len(A[i])):
        if (i == j and A[i][j] != 1) or (i != j and A[i][j] != 0):
            eh_identidade = False
            break
    if not eh_identidade:
        break

print("A matriz e identidade" if eh_identidade else "A matriz nao e identidade")