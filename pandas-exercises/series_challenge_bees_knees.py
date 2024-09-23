import numpy as np
import pandas as pd

bees = pd.Series([True, True, False, np.nan, True, False, True, np.nan])
print(bees)

knees = pd.Series([5, 2, 9, 1, 3, 10, 5, 2], index = [7, 0, 2, 6, 3, 5, 1, 4])
print(knees)

# if the ith value of bees is NaN, double the ith value inside knees

# mask = (bees.isna())
# knees_reset = knees.reset_index(drop=True)
# knees_reset[mask] = knees_reset[mask] * 2
# print(knees_reset)

# Or (better)

knees.loc[pd.isna(bees).to_numpy()] *= 2
print(knees)