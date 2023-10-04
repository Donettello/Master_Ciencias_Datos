# Número decimal a convertir en formato IE3
numero = "53.2874"

# Dividimos en parte entera y decimal
entero, decimal = numero.split(".")

# Hacemos conversion de tipo desde texto.
entero = int(entero)
decimal = float("0." + decimal)

# Obtención del signo
if entero >= 0:
    signo = 0
else:
    signo = 1
    entero = abs(entero)

# Calculamos los binarios de las partes del número
entero = str(bin(entero)[2:])

d_b = ""
for _ in range(len(entero), 24):
    decimal *= 2
    if decimal < 1.:
        d_b += "0"
    else:
        d_b += "1"
        decimal -= 1.

# Obtenemos el valor del exponente
if entero[0] != 0:
    # El valor absoluto del número es mayor que 1
    exponencial = bin(127 + len(entero) -1)[2:]
    
    pass
else:
    # El valor absoluto del número es menor que 1
    pass

print(entero, d_b)