import numpy as np

A = np.array([[2, 0, 0],
              [0, 1, 0],
              [0, 0, 7]])

eh_diagonal = True

for i in range(len(A)):
    for j in range(len(A[i])):
        if i != j and A[i][j] != 0:
            eh_diagonal = False
            break
    if not eh_diagonal:
        break

print("A matriz e diagonal" if eh_diagonal else "A matriz nao e diagonal")