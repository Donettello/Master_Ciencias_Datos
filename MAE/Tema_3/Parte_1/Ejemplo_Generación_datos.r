# Parámetros
beta0 <- 0
beta1 <- 1
sigma <- 4

# Muestra original de (x, y)
set.seed(100)
x <- seq(-20, 20, 0.2)
n <- length(x)
epsilon <- rexp(n, rate = 1/sigma)
y <- beta0 + beta1*x + epsilon
summary(lm(y~x))

# Desviación típica verdadera
dt_beta1 <- sigma / sqrt(sum((x-mean(x))^2))
dt_beta1
# Representación gráfica
ggplot(data.frame(x, y), aes(x, y)) +
  geom_point() +
  geom_smooth(method = lm)
