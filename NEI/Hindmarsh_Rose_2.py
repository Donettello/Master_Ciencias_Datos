import matplotlib.pyplot as plt

# Función hindmarsh_rose
def hindmarsh_rose(t_end, dt, y0, ei=3.0):
    t = 0
    x, y, z = y0
    results = [[t, x, y, z]]
    
    while t < t_end:
        dxdt = y + 3 * x ** 2 - x ** 3 - z + ei
        dydt = 1 - 5 * x ** 2 - y
        dzdt = 0.0021 * (-z + 4 * (x + 1.6))
        
        x += dxdt * dt
        y += dydt * dt
        z += dzdt * dt
        
        t += dt
        results.append([t, x, y, z])
    
    return results

# Definir condiciones iniciales
y0 = [0, 0, 0]  # [x0, y0, z0]

# Tiempo final de integración
t_end = 10  # Tiempo final de integración

# Tamaño del paso de tiempo
dt = 0.001  # Tamaño del paso de tiempo

# Parámetro opcional ei
ei = 3.0

# Usar la función hindmarsh_rose
resultados = hindmarsh_rose(t_end, dt, y0, ei)

# Extraer resultados para graficar
t_values = [result[0] for result in resultados]
x_values = [result[1] for result in resultados]
y_values = [result[2] for result in resultados]
z_values = [result[3] for result in resultados]

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label='x')
plt.plot(t_values, y_values, label='y')
plt.plot(t_values, z_values, label='z')
plt.title('Soluciones de las Ecuaciones de Hindmarsh-Rose')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()