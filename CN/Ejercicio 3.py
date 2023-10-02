def kahansum(xs):
    s = 0.; e = 0.
    for x in xs:
        temp = s
        y = x + e # realizo la compensacion
        s = temp + y
        e = (temp - s) + y #calculo la nueva compensacion
    return s

xs = [0.7, 0.3, 0.1]
print(kahansum(xs))
print(sum(xs))