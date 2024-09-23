import pandas as pd
import numpy as np

# CREAZIONE DI SERIE E DATAFRAME
# Serie Pandas con indici personalizzati
serie = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Serie Pandas:")
print(serie)

# Creazione di un DataFrame
data = {
    'Nome': ['Paolo', 'Maria', 'Luigi'],
    'Età': [23, 35, 30],
    'Città': ['Roma', 'Milano', 'Napoli']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# INFORMAZIONI SU SERIE E DATAFRAME
# Dimensioni del DataFrame
print(f"Dimensioni del DataFrame: {df.shape}")
# Tipo di dati delle colonne
print("Tipi di dati delle colonne:")
print(df.dtypes)
# Descrizione statistica delle colonne numeriche
print("Descrizione statistica del DataFrame:")
print(df.describe())

# ACCESSO AI DATI
# Accesso a una colonna nel DataFrame
print("Colonna 'Nome':")
print(df['Nome'])
# Accesso a una riga per indice numerico con .iloc (posizione)
print("Prima riga del DataFrame:")
print(df.iloc[0])
# Accesso a una riga per label con .loc (condizione)
print("Persone con età superiore a 30:")
print(df.loc[df['Età'] > 30])

# ACCESSO A UNA SERIE PANDAS
# Accesso per label (indice personalizzato)
print("Elemento con label 'c' in Pandas Series:", serie['c'])
# Accesso per indice numerico (posizione) con .iloc
print("Elemento con indice 2 in Pandas Series:", serie.iloc[2])
# Slicing per label
print("Slicing da 'b' a 'd' in Pandas Series:")
print(serie['b':'d'])
# Mascheramento: elementi maggiori di 30
print("Elementi maggiori di 30 in Pandas Series:")
print(serie[serie > 30])

# USO DI .LOC PER SELEZIONE E MASCHERAMENTO
# Creazione di una Serie con valori casuali
numeri = pd.Series([20, 50, 11, 45, 17, 31])
print("Serie di numeri:")
print(numeri)

# Maschera condizionale
print("Maschera per valori minori di 20:")
mask = numeri < 20
print(mask)

# Accesso tramite maschera con .loc
print("Elementi minori di 20 in Serie Pandas usando .loc:")
print(numeri.loc[mask])

# Accesso diretto a un elemento tramite indice con .loc
print("Elemento con indice 0 nella Serie Pandas usando .loc:")
print(numeri.loc[0])

# TRASFORMARE NPARRAYS IN SERIE PANDAS
array_numeri = np.array([10, 20, 30, 40])
serie_da_array = pd.Series(array_numeri)
print("Serie creata da array NumPy:")
print(serie_da_array)

# AGGIUNGERE O RIMUOVERE DATI IN UN DATAFRAME
# Aggiungere una nuova colonna
df['Professione'] = ['Ingegnere', 'Avvocato', 'Medico']
print("DataFrame con nuova colonna 'Professione':")
print(df)

# Rimuovere una colonna
df = df.drop(columns=['Città'])
print("DataFrame dopo aver rimosso la colonna 'Città':")
print(df)

# Rimuovere una riga per indice
df = df.drop(index=0)
print("DataFrame dopo aver rimosso la prima riga:")
print(df)

# ORDINAMENTO E FILTRO
# Ordinare per colonna
print("DataFrame ordinato per 'Età':")
print(df.sort_values(by='Età'))
# Filtro condizionale su una colonna
print("DataFrame filtrato per nome 'Luigi':")
print(df[df['Nome'] == 'Luigi'])

# GESTIONE DI VALORI MANCANTI
df_nan = pd.DataFrame({
    'Nome': ['Anna', 'Marco', 'Luca'],
    'Età': [28, None, 25],
    'Città': [None, 'Firenze', 'Roma']
})
print("DataFrame con valori NaN:")
print(df_nan)

# Riempire i valori mancanti con un valore predefinito
df_nan_filled = df_nan.fillna("Sconosciuto")
print("DataFrame dopo aver riempito i NaN con 'Sconosciuto':")
print(df_nan_filled)

# Eliminare righe con valori NaN
df_nan_dropped = df_nan.dropna()
print("DataFrame dopo aver eliminato le righe con NaN:")
print(df_nan_dropped)

# UNIONE E CONCATENAZIONE DI DATAFRAME
df1 = pd.DataFrame({'ID': [1, 2], 'Nome': ['Giulia', 'Francesco']})
df2 = pd.DataFrame({'ID': [1, 2], 'Età': [29, 33]})
# Unione di due DataFrame su una colonna comune
df_merged = pd.merge(df1, df2, on='ID')
print("DataFrame unito:")
print(df_merged)

# Concatenazione di DataFrame
df3 = pd.DataFrame({'Nome': ['Carlo'], 'Età': [40]})
df_concat = pd.concat([df_merged, df3], ignore_index=True)
print("DataFrame concatenato:")
print(df_concat)