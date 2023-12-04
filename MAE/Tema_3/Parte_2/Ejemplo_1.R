library(MASS)

set.seed(12)
n <- 100
rho <- 0.995
Sigma <- matrix(c(1, rho, rho, 1), 2)
x <- mvrnorm(n, mu = c(0,0), Sigma = Sigma)
x1 <- x[,1]
x2 <- x[,2]
y <- x1 + x2 + rnorm(n, sd=4)

datos <- data.frame(y, x1, x2)
summary(lm(y ~ x1 + x2, data = datos))
