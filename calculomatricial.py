import numpy as np

# Definindo a matriz A
A = np.array([[2, 3, -1], [4, 1, 2], [3, 2, 3]])

# Definindo o vetor b
b = np.array([1, 2, 3])

# Resolvendo o sistema linear Ax = b
x = np.linalg.solve(A, b)

# Exibindo a solução
print('A solução do sistema é:')

print(x)
