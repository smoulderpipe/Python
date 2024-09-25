import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [5.2, 1.7, 9.4],
    "B": [3.9, 4.0, 7.8]
})
print(df)

def my_func(x):
    return x

df["C"] = df["A"].apply(my_func)
print(df)

print(df.apply(func=np.sum, axis=0))

kids = pd.DataFrame({
    "name" : pd.Series(["alice", "mary", "jimmy", "johnny", "susan"], dtype="string"),
    "age" : [9, 13, 11, 15, 8],
    "with_adult" : [True, False, False, True, True]
})
print(kids)

# Only kids with_adult or kids > 12 years of age can enter

kids["enter"] = kids["with_adult"] | (kids["age"] > 12)
print(kids.loc[kids["enter"]])

# Or (using APPLY)

def is_allowed(kids_series):
    return kids_series.loc["age"] >= 12 or kids_series.loc["with_adult"]

print(kids.apply(is_allowed, axis=1))

# Or (using APPLY + lambda)

def is_allowed2(age, with_adult):
    return age >= 12 or with_adult

print(kids.apply(lambda row: is_allowed2(row.loc["age"], row.loc["with_adult"]), axis=1))