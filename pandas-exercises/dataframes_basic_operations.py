import pandas as pd
import numpy as np

df = pd.DataFrame({
    "a": [2, 3, 11, 13],
    "b": ["fox", "rabbit", "hound", "rabbit"]
})
print(df)

# Creazione di una nuova colonna

df["c"] = np.arange(4)
print(df)

df["d"] = df["a"] + df["c"]
print(df)

df.loc[df.b == "rabbit", "f"] = 0
print(df)

# Eliminazione di una colonna

df.drop(columns = ["f"], inplace=True)
print(df)


