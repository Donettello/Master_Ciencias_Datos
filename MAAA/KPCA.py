import numpy as np
from math import *
from sklearn.datasets import make_blobs
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import KernelCenterer
from scipy.sparse.linalg import eigs
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
        # Computation of the projection direction
        if self.kernel == "linear":
            self.kernel_matrix = np.dot(np.transpose(X), X)


            eigvals, eigvecs = eigs(self.kernel_matrix)
            self.eigvals, self.eigvecs = eigvals[::-1], eigvecs[:,::-1]

            self.projected = np.column_stack([self.eigvecs[i, :] for i in range(self.n_components)])
        elif self.kernel == "rbf":
            if self.gamma is None:
                # Calcular la mediana de las distancias entre pares de puntos
                pairwise_distances = np.linalg.norm(X[:, np.newaxis] - X, axis=2)
                median_distance = np.median(pairwise_distances)
                
                # Usar la mediana como gamma
                self.gamma = 1.0 / (2.0 * median_distance ** 2)
            
            # Calcular la matriz de kernel RBF
            kernel_matrix = rbf_kernel(X, X, gamma=self.gamma)
        
            # Centrar el kernel utilizando KernelCenterer
            kernel_centerer = KernelCenterer()
            centered_kernel = kernel_centerer.fit_transform(kernel_matrix)

            # Almacenar X_fit_
            self.X_fit_ = X

            # Calcular los eigenvectores y eigenvalores
            eigvals, eigvecs = np.linalg.eigh(centered_kernel)
            
            # Ordenar los eigenvectores en orden descendente de eigenvalores
            sorted_indices = np.argsort(eigvals)[::-1]
            eigvals = eigvals[sorted_indices]
            eigvecs = eigvecs[:, sorted_indices]
            
            # Tomar los primeros n_components eigenvectores
            self.eigvecs_ = eigvecs[:, :self.n_components]
        else:
            raise ValueError("Unsupported kernel type")
        return self

    def transform(self, X):
        # Computation of the projected components
        if self.kernel == "linear":
            return np.dot(X, self.eigvecs[:, :self.n_components])
        elif self.kernel == "rbf":
             # Calcular el kernel entre los nuevos datos y los datos originales
            kernel_new_data = rbf_kernel(X, self.X_fit_, gamma=self.gamma)
    
            # Proyectar los nuevos datos en el espacio de las componentes principales
            projected_data = np.dot(kernel_new_data, self.eigvecs_)
            
            return projected_data
        else:
            raise ValueError("Unsupported kernel type")

    def fit_transform(self, X):
        # Computation of the projected components over X just after training with it
        self.fit(X)
        return self.transform(X)

def compValues(X, Y):
    return np.array_equal(np.sort(X), np.sort(Y))

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
'''
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
'''print("Comparativas de autovectores mediante correlación:")
correlation = np.corrcoef(np.transpose(model_my.eigvecs_), np.transpose(model_sk.eigenvectors_))
print("Correlación entre las componentes principales:")
print(correlation)'''

print("Proyección")
print("Proyección propia:")
print(model_my.transform(X_new))
print("Proyección sklearn:")
print(model_sk.transform(X_new))