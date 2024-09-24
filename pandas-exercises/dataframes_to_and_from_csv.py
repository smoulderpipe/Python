import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": np.arange(1000),
    "b": np.random.normal(size=1000),
    "c": pd.Series(np.random.choice(["cat", "dog", "hippo"], size=1000, replace=True))
})
print(df)

df.to_csv("pets.csv", index=False)

pets = pd.read_csv("pets.csv")
print(pets)