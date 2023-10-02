import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

"""
x = np.array([0, 2, 5])
y = np.array([-2,2,6])
poly = lagrange(x, y)

print(Polynomial(poly).coef)
"""
x = np.arange(-1,1.1,.01)
y = -x**2
plt.plot(x,y,'r')
y = -x**2 + np.random.normal(0,0.15,len(x))
plt.plot(x[::10],y[::10],'ro')
X=x[::10]
Y=y[::10]
poly = lagrange(X, Y)
Y=poly(x)
plt.plot(x,Y,'g')
plt.ylim(-1.5,.5)

plt.show()
