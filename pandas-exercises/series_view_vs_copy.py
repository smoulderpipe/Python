import pandas as pd
import numpy as np

x = pd.Series(
    data = [2, 3, 5, 7, 11],
    index = [2, 11, 12, 30, 30])
print(x)

# Creiamo una view di x (ovvero una reference a x)
y = x

y.iloc[0] = 99

# Se cambiamo y, cambia anche x, perché y è solo un riferimento (view) a x
print("\nSerie y dopo la modifica:")
print(y)
print("\nSerie x dopo la modifica a y (anch'essa modificata):")
print(x)

# Creiamo una copia di x
z = x.copy()

z.iloc[0] = np.nan

# Se cambiamo z, x non cambia perché z è una copia indipendente
print("\nSerie z dopo la modifica (x non cambia):")
print(z)
print("\nSerie x rimane invariata:")
print(x)

# Uso di loc per creare una "view" basata su condizione
w = x.loc[x < 30]

# Il valore di w non cambia il valore di x
w.iloc[0] = 100
print("\nSerie w dopo la modifica:")
print(w)
print("\nSerie x rimane invariata (nessuna modifica a x):")
print(x)

# REPLACE

zoo = pd.Series(
    ["tiger", "lion", "zebra", "lion"])
print(zoo)

# L'uso di replace genera una nuova serie, non modificando l'originale
farm = zoo.replace({"lion": "hamster", "tiger": "bunny"})
print(zoo)
print(farm)

# Se vogliamo modificare anche l'originale:
zoo.replace({"lion": "hamster", "tiger": "bunny"}, inplace=True)
print(zoo)