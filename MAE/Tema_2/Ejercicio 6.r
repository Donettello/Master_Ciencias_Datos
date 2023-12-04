muestra <- c(1, 2, 3.5, 4, 7, 7.3, 8.6, 12.4, 13.8, 18.1)
n <- length(muestra)
B <- 1000 # Este valor es el que hay que cambiar
res <- replicate(10, sd(replicate(B, mean(sort(sample(muestra, n, replace=T)[3:8])))))
res

