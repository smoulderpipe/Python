import pandas as pd
import numpy as np

# EFFICIENT DTYPES

# Creiamo una Series (avrà dtype float64)
ages_float64 = pd.Series([25, 30, np.nan, 40, None])
print("Serie con dtype int64:")
print(ages_float64)

# Creiamo una Series con dtype Int64 (avrà dtype Int64)
ages_Int64 = pd.Series([25, 30, np.nan, 40, None], dtype='Int64')
print("\nSerie con dtype Int64:")
print(ages_Int64)

# Creiamo una Series di stringhe usando dtype object (inefficiente)
names_object = pd.Series(["Alice", "Bob", None, np.nan, "Eva"])
print("\nSerie di stringhe con dtype object:")
print(names_object)

# Creiamo una Series di stringhe usando pd.StringDtype (efficiente)
names_string = pd.Series(["Alice", "Bob", None, np.nan, "Eva"], dtype=pd.StringDtype())
print("\nSerie di stringhe con pd.StringDtype:")
print(names_string)

# MISSING VALUES

data = pd.Series([10, np.nan, 20, None, 30])
print("Serie originale:")
print(data)

# Riempire i valori nulli con un valore specifico (ad esempio, 0)
filled_data = data.fillna(0)
print("\nSerie dopo fillna(0):")
print(filled_data)

print("\nValori nulli (pd.isna):")
print(pd.isna(data))

print("\nValori non nulli (pd.notna):")
print(pd.notna(data))

# Riempire i valori nulli con la media della serie
mean_value = data.mean()
filled_with_mean = data.fillna(mean_value)
print("\nSerie dopo fillna(mean):")
print(filled_with_mean)