import numpy as np

A=np.array([[1,2,3],[3,2,1],[-2,0,2],[4,4,4]])
u,s,vh=np.linalg.svd(A)
print(u.shape, s.shape, vh.shape)
print(u)
print(s)
print(vh)
smat = np.zeros((4, 3))
smat[:3, :3] = np.diag(s)
print(smat)
print(np.allclose(A, np.dot(u, np.dot(smat, vh))))