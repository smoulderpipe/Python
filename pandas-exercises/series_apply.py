import pandas as pd
import numpy as np

foo = pd.Series([3, 9, 2, 2, 8, 7])
print(foo)

def my_func(x):
    return x - 1 if x % 2 == 0 else x + 3

# Il metodo apply permette di applicare una funzione ai singoli elementi di una serie
# Non è efficiente in termini di velocità perché non è vettorializzato
print(foo.apply(my_func))

# Molto meglio:
a = foo.to_numpy()
y1 = pd.Series(np.where(a % 2 == 0, a -1, a + 3))
print(y1)