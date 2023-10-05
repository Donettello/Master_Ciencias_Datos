# Número decimal a convertir en formato IE3
#numero = "53.2874"
#numero = "1.0"
numero = "0.5"

# Dividimos en parte entera y decimal
entero, decimal = numero.split(".")

# Hacemos conversion de tipo desde texto.
entero = int(entero)
decimal = float("0." + decimal)

# Obtención del signo
if entero >= 0:
    signo = '0'
else:
    signo = '1'
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
if entero[0] != '0':
    # El valor absoluto del número es mayor que 1
    exponencial = bin(127 + len(entero) -1)[2:]
    mantisa = entero[1:] + d_b
    pass
else:
    # El valor absoluto del número es menor que 1
    exponencial = bin(127 - (d_b.index('1')+1))[2:]
    mantisa = d_b[1:]
    mantisa += ("0" * (23 - len(mantisa)))
    pass

relleno = "0" * (8 - len(exponencial))
print(signo, relleno + exponencial, mantisa)
print(len(signo)+len(relleno)+len(exponencial)+len(mantisa))