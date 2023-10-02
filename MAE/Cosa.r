library(tidyverse)
# P(Z > 1)
1 - pnorm(1)
# P(X > x) = 0.3
qnorm(0.7)
# Mediana de exponencial de media 2
qexp(0.5, rate=0.5)
# Números aleatorios
set.seed(9999)
x <- rnorm(10000)
df <- data.frame(x=x)
ggplot(df) + 
  geom_histogram(aes(x=x, y=..density..),
                 col='black', fill='lightblue', bins=10) +
  geom_function(fun = dnorm, col='black', size=1.3)