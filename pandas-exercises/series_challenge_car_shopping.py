import pandas as pd
import numpy as np

asking_prices = pd.Series([5000, 7600, 9000, 8500, 7000], index=["civic", "civic", "camry", "mustang", "mustang"])
print(asking_prices)

fair_prices = pd.Series([5500, 7500, 7500], index=["civic", "mustang", "camry"])
print(fair_prices)

#identify cars whose asking price is less than the fair price

asking_prices_aggregated = asking_prices.groupby(asking_prices.index).min()
asking_prices_realigned = asking_prices_aggregated.reindex(fair_prices.index)
mask = asking_prices_realigned < fair_prices
result = asking_prices_realigned[mask]
print(result)

#or

all_fair_prices = fair_prices.loc[asking_prices.index]
off_market_prices = asking_prices - all_fair_prices
below_fair_prices = (off_market_prices < 0).reset_index(drop=True)
print(below_fair_prices.loc[below_fair_prices].index.to_list())