import pandas as pd
import numpy as np

df = pd.DataFrame({
    "shrimp": [10, 20, 30, 40, 50, 60],
    "crab": [5, 10, 15, 20, 25, 30],
    "red_fish": [2, 3, 5, 7, 11, 13]
})
print(df)

#access individual columns or rows and their elements

print(df["shrimp"])
print(df.shrimp)
print(df[["shrimp", "crab"]])
print(df.loc[1]) # returns a series
print(df.loc[[1]]) # returns a dataframe
print(df.loc[1:3])
print(df.iloc[:, [0, 1]])

df.index = ["a", "b", "c", "d", "e", "f"]
print(df)
print(df.loc[["b", "e"]])
print(df.loc[["a", "c", "f"], ["crab", "shrimp"]])
print(df.iloc[:3, [df.columns.get_loc(c) for c in ['shrimp', 'red_fish']]])
print(df.columns)

#boolean indexing

mask = df.shrimp < 40
print(mask)
print(df.loc[mask])