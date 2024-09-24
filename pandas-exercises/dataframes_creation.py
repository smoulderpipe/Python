import numpy as np
import pandas as pd

# Un modo per creare un dataframe:
df = pd.DataFrame({
    "name": ["Bob", "Sue", "Mary"],
    "age": [39, 57, 20]
})
print(df)

# Un altro modo: crearlo come lista di liste
df2 = pd.DataFrame(
    [
        ["Bob", 39],
        ["Sue", 57],
        ["Mary", 20]
    ], columns=["name", "age"]
)
print(df2)

# Ottenere info sul dataframe:
print(df.info())
print(df.shape)
print(df.axes)
print(df.size)

# Rinominare le colonne:
df.rename(columns={"age":"years"}, inplace=True)
print(df)