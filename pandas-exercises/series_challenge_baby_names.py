import pandas as pd
import numpy as np

babynames = pd.Series(["Jathonathon", "Zeltron", "Ruger", "Phreddy", "Chad", "Chad", "Phreddy", "Ruger", "Ryan",
                       "Phreddy", "Phreddy", "Phreddy", "Mister", "Zeltron", "Ryan", "Ruger", "Ruger", "Jathonathon",
                       "Jathonathon", "Ruger", "Chad", "Zeltron"], dtype="string")

# Determine how many people voted for the following names: 'Chad', 'Ruger', 'Zeltron'

name_counts = babynames.value_counts()

print(f"Number of votes for 'Chad': {name_counts.get("Chad", 0)}")
print(f"Number of votes for 'Ruger': {name_counts.get("Ruger", 0)}")
print(f"Number of votes for 'Zeltron': {name_counts.get("Zeltron", 0)}")

# Or

print(babynames.value_counts().loc[["Chad", "Ruger", "Zeltron"]])