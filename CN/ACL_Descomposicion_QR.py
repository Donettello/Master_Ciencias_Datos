import numpy as np
A = np.array([[1, 2, 3],
              [3, 1, 2],
              [1, 3, 1]])
Q, R = np.linalg.qr(A)
print(Q)
print(R)
