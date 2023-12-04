natalidad <- read.table("https://verso.mat.uam.es/~joser.berrendero/datos/natalidad.txt", header = TRUE) %>% 
  mutate(log_pnb = log(pnb))

reg <- lm(esph ~ nat  + mortinf + log_pnb, data = natalidad)
summary(reg)

#a) df = n-p-1 => n = df +p+1 = 87 + 3 + 1 = 91
#b) 
#f)
vcov(reg)
