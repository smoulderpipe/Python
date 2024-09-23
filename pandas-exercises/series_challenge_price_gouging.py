import pandas as pd
import numpy as np

generator = np.random.default_rng(123)
beef_prices = pd.Series(
    data = np.round(generator.uniform(low=3, high=5, size=10), 2),
    index = generator.choice(10, size = 10, replace=False)
)
print(beef_prices)

# Trova una lista che rappresenti l'aumento del prezzo del manzo in percentuale rispetto al giorno precedente

beef_prices.sort_index(inplace=True)
price_increase = 100 * (beef_prices - beef_prices.shift(1)) / beef_prices.shift(1)

print(price_increase)
print(price_increase.idxmax())