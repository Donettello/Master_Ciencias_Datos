import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Definir las ecuaciones diferenciales de Hindmarsh-Rose
def hindmarsh_rose(t, y, ei=3.0):
  x, y, z = y
  dxdt = y + 3 * x ** 2 - x ** 3 - z + ei
  dydt = 1 - 5 * x ** 2 - y
  dzdt = 0.0021 * (-z + 4 * (x + 1.6))

  return [dxdt, dydt, dzdt]

y0 = [0, 0, 0]
t_span = (0, 10000)
t_eval = np.linspace(*t_span, 10000)

# Resolver las ecuaciones diferenciales
sol = solve_ivp(hindmarsh_rose, t_span, y0, t_eval=t_eval, args=(3,))

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(sol.t[2000:3000], sol.y[0, 2000:3000], label='x(t)')
#plt.plot(sol.t[1000:6500], sol.y[1, 1000:6500], label='y(t)')
plt.plot(sol.t[2000:3000], sol.y[2, 2000:3000], label='z(t)')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Valor')
plt.title('Hindmarsh-Rose con todas las nuevas ecuaciones (rango 10000-13000)')
plt.legend()
plt.grid(True)
plt.show()