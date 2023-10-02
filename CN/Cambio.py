numero = "53.2874"

entero, decimal = numero.split(".")

entero = int(entero)
decimal = float("0." + decimal)

entero = str(bin(entero)[2:])

d_b = ""
for _ in range(len(entero), 24):
    decimal *= 2
    if decimal < 1.:
        d_b += "0"
    else:
        d_b += "1"
        decimal -= 1.

print(entero, d_b)