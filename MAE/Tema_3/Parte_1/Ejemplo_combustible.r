library(dplyr)
datos <- 'http://verso.mat.uam.es/~joser.berrendero/datos/combustible.RData'
load(url(datos))
head(fuel2001)

fuel2001 <- fuel2001 %>% 
  mutate(Fuel = 1000 * FuelC/Pop) %>% 
  mutate(Dlic = 1000 * Drivers/Pop) %>% 
  mutate(logMiles = log(Miles))

# Diagramas de dispersión
library(GGally)
ggpairs(fuel2001) +
  theme(axis.text=element_blank())

reg <- lm(Fuel ~ Tax + Dlic + Income + logMiles,
          data=fuel2001)
summary(reg)

nuevo.dato <- data.frame(18, 1031, 23471, 11)
names(nuevo.dato) <- names(fuel2001)[c(7, 9, 3, 10)]
nuevo.dato

predict(reg, nuevo.dato, interval='confidence')

predict(reg, nuevo.dato, interval='prediction')

# Modelo completo
reg <- lm(Fuel ~ Tax + Dlic + Income + logMiles,
          data=fuel2001)

# Modelo reducido
reg0 <- lm(Fuel ~ logMiles, data=fuel2001)
anova(reg0)
