import pandas as pd
import numpy as np

#INDICIZZAZIONE BOOLEANA TRAMITE INDICI E TRAMITE POSIZIONI

serie_pandas = pd.Series([20, 50, 11, 45, 17, 31])
print("Serie Pandas originale:")
print(serie_pandas)

array_numpy = np.array([20, 50, 11, 45, 17, 31])
print("\nArray Numpy originale:")
print(array_numpy)

# Creazione di una maschera per trovare i valori minori di 20
mask = serie_pandas < 20
print("\nMaschera per valori < 20 nella Serie Pandas (True/False):")
print(mask)

print("\nValori < 20 selezionati con la maschera (usando .loc):")
print(serie_pandas.loc[mask])

print("\nAccesso al primo elemento della Serie (indice 0):")
print(serie_pandas.loc[0])

print("\nValori < 20 direttamente con la condizione all'interno di .loc:")
print(serie_pandas.loc[serie_pandas < 20])

# Modifica degli indici della Serie Pandas per dimostrare come l'indice influisce sull'accesso ai dati
serie_pandas.index = [0, 1, 2, 3, 5, 4]
print("\nSerie Pandas dopo modifica degli indici (disordinati):")
print(serie_pandas)

# Attenzione: usiamo .loc con la maschera originale, ma a causa degli indici disordinati, il risultato potrebbe essere fuorviante
# Include erroneamente il numero 31 perché l'indice è cambiato, ma la maschera no
print("\nUso di .loc con la maschera originale (può produrre risultati sbagliati a causa degli indici modificati):")
print(serie_pandas.loc[mask])

# Soluzione corretta: convertiamo la maschera in un array NumPy per selezionare i valori basandoci sulla posizione e non sull'indice
print("\nUso corretto: maschera convertita in array Numpy per filtrare correttamente i valori:")
print(serie_pandas.loc[mask.to_numpy()])

#COMBINAZIONI DI SERIE BOOLEANE

ages = pd.Series(
    data = [42, 43, 13, 18, 1],
    index = ["peter", "lois", "chris", "meg", "stewie"]
)
print(ages)

genders = pd.Series(
    data = ["female", "female", "male", "male", "male"],
    index = ["lois", "meg", "chris", "peter", "stewie"],
    dtype= "string"
)
print(genders)

#who's a male younger than 18?

#deprecated (future warning in console):
#mask = (genders == "male") & (ages < 18)
#mask.loc[mask]
#print(mask)

#better:
aligned_ages = ages.reindex(genders.index)
mask = (genders == "male") & (aligned_ages < 18)
print(mask[mask])