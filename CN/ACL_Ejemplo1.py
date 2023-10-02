import numpy as np
a=np.array([[3,-np.sqrt(2)],[-np.sqrt(2),2]])
l,v=np.linalg.eig(a)
print(l)
print(v)