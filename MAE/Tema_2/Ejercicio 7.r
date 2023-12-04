muestra <- c(1, 2, 3.5, 4, 7, 7.3, 8.6, 12.4, 13.8, 18.1)
var_original = var(muestra)

# a) Usar bootstrap para determinar el error del estimados sigma^2.
B <- 1000
muestras_bootstrap <- sample(muestra, n*B, rep= T)
muestras_bootstrap <- matrix(muestras_bootstrap, nrow=n)
var_bootstrap <- apply(muestras_bootstrap, 2, var)

# Error típico
sd(var_bootstrap)

# b)Suponindo normalidad -> Lema de Fisher
sqrt(2*var_original^2 / (n-1))

#c)
alfa <- 0.05
T_bootstrap <- sqrt(n) * (var_bootstrap - var_original)
ic_min = var_original - quantile(T_bootstrap, 1-alfa/2)/sqrt(n)
ic_max = var_original - quantile(T_bootstrap, alfa/2)/sqrt(n)

c(ic_min, ic_max)

# IC bajo normalidad
(n-1) * var(muestra) * c(1/qchisq(1-alfa/2, n-1), 1/qchisq(alfa/2, n-1))
