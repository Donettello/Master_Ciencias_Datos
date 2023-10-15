import numpy as np
from math import *
from sklearn.datasets import make_blobs
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.preprocessing import StandardScaler
from scipy.sparse.linalg import eigs
from scipy.spatial.distance import pdist, squareform
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('figure', figsize=(15, 5))
seed = 123

class KPCA():
    """
        Kernel PCA.
    """
    def __init__(self, n_components, kernel="rbf", gamma=None):
        # Assignment of the hyper-parameters
        self.n_components = n_components
        self.kernel = kernel
        self.gamma = gamma

    def fit(self, X):
        # Comprobamos el tipo de kernel
        if self.kernel == "linear":
            self.kernel_matrix = np.dot(np.transpose(X), X)
            # self.kernel_matrix = pairwise_kernels(X, metric=self.kernel)
            
        elif self.kernel == "rbf":
            # Usar rbk_ker

            # Pasar KernelCenterer
            
            # Hacer fit
            pass
        else:
            raise ValueError("Unsupported kernel type")

        eigvals, eigvecs = eigs(self.kernel_matrix)
        self.eigvals, self.eigvecs = eigvals[::-1], eigvecs[:,::-1]

        self.projected = np.column_stack([self.eigvecs[:, i] for i in range(self.n_components)])
        return self

    def transform(self, X):
        # Computation of the projected components
        if self.kernel == "linear":
            return np.dot(X, self.eigvecs[:, :self.n_components])
        elif self.kernel == "rbf":
            # Hacer el método transform
            pass
        else:
            raise ValueError("Unsupported kernel type")

    def fit_transform(self, X):
        # Computation of the projected components over X just after training with it
        self.fit(X)
        return self.transform(X)
    
X, y = make_blobs(random_state=seed)
X_train = X[:90,:]; y_train=y[:90]
X_new = X[90:,:]; y_new=y[90:]

plt.scatter(X_train[:,0], X_train[:,1],c=y_train, label='train')
plt.scatter(X_new[:,0], X_new[:,1], c=y_new, marker='s', label='new')
plt.legend()
#plt.show()

# Procesamos los datos
scaler = StandardScaler()
scaler.fit(X_train)
X_scaler = scaler.transform(X_train)

# Hiperparámetros de los KPCA's
kernel = 'linear'
n_components=1

model_my = KPCA(n_components=n_components, kernel=kernel)
model_sk = PCA(n_components=n_components)

# Training of the models (complete).
model_my.fit(X_scaler)
model_sk.fit(X_scaler)

print("Comparativa de autovectores")
print("Autovectores implementados:")
print(model_my.projected)
print("Autovectores sklearn:")
print(model_sk.components_)
print("Comparativa de proyecciones")
print("Proyección propia:")
print(model_my.transform(X_new))
print("Proyección sklearn:")
print(model_sk.transform(X_new))
print("=================================================")
'''
kernel = 'rbf'
n_components=1

# Model definition (complete).
model_my = KPCA(n_components=n_components, kernel=kernel)
model_sk = KernelPCA(n_components=n_components)

# Training of the models (complete).
model_my.fit(X_scaler)
model_sk.fit(X_scaler)

# Comparative of the eigenvectors (complete).
print("Comparativas de autovectores")
print("Autovector propio:")
print(model_my.projected)
print("Autovector sklearn:")
print(model_sk.eigenvectors_)

# Comparative of the projections (complete).
print("Comparativas de proyecciones")
print("Proyección propia:")
print(model_my.transform(X_new))
print("Proyección sklearn:")
print(model_sk.transform(X_new))'''