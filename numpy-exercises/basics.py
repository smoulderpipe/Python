import numpy as np

# Creazione di array 1D
arr = np.array([10, 20, 30, 40, 50])
print("Array 1D:")
print(arr)
print(f"Dimensionalità: {arr.ndim}")
print(f"Forma: {arr.shape}")
print(f"Dimensione totale (numero di elementi): {arr.size}")
print(f"Tipo di dati: {arr.dtype}")

# Creazione di array 2D
arr_2d = np.array([
    [10, 20, 30, 40, 50],
    [70, 80, 90, 100, 200]
])
print("Array 2D:")
print(arr_2d)
print(f"Dimensionalità: {arr_2d.ndim}")
print(f"Forma: {arr_2d.shape}")
print(f"Dimensione totale: {arr_2d.size}")
print(f"Tipo di array: {type(arr_2d)}")
print(f"Tipo di dati: {arr_2d.dtype}")
print(f"Elementi della prima riga: {arr_2d[0]}")
print(f"Elementi della prima colonna: {arr_2d[:, 0]}")
print(f"Tutti gli elementi ogni 2 (array appiattito): {arr_2d.flatten()[::2]}")

# Slicing su array 1D e 2D
print("Slicing su array 1D e 2D:")
print(f"Elementi dal 2° al 4° in arr: {arr[1:4]}")  # Slicing su array 1D
print(f"Elementi dal 2° al 4° in arr_2d, prima riga: {arr_2d[0, 1:4]}")  # Slicing su array 2D
print(f"Ultima colonna in arr_2d: {arr_2d[:, -1]}")

# Reshape di array
print("Reshape e appiattimento:")
arr_reshaped = np.arange(12).reshape(3, 4)  # Crea un array di numeri consecutivi da 0 a 11 e lo risistema in un array 3x4
print(f"Array reshaped (3x4):\n{arr_reshaped}")
print(f"Array appiattito (flatten): {arr_reshaped.flatten()}")

# Operazioni matematiche base su array
print("Operazioni matematiche base:")
arr_sum = arr + 5  # Somma di 5 a tutti gli elementi
print(f"Somma di 5 a ogni elemento: {arr_sum}")
arr_square = arr ** 2  # Elevamento al quadrato
print(f"Elementi al quadrato: {arr_square}")
arr_sum_total = np.sum(arr)  # Somma totale degli elementi
print(f"Somma totale degli elementi: {arr_sum_total}")
arr_mean = np.mean(arr)  # Media degli elementi
print(f"Media degli elementi: {arr_mean}")
arr_max = np.max(arr)  # Massimo
print(f"Massimo valore: {arr_max}")
arr_min = np.min(arr)  # Minimo
print(f"Minimo valore: {arr_min}")

# Operazioni tra array
print("Operazioni tra array:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_add = arr1 + arr2  # Somma tra array
print(f"Somma tra array: {arr_add}")
arr_mul = arr1 * arr2  # Moltiplicazione elemento per elemento
print(f"Moltiplicazione elemento per elemento: {arr_mul}")
arr_dot = np.dot(arr1, arr2)  # Prodotto scalare
print(f"Prodotto scalare tra arr1 e arr2: {arr_dot}")

# Funzioni di aggregazione su array 2D
print("Funzioni di aggregazione su array 2D:")
print(f"Somma lungo le righe: {np.sum(arr_2d, axis=1)}")
print(f"Somma lungo le colonne: {np.sum(arr_2d, axis=0)}")
print(f"Media lungo le righe: {np.mean(arr_2d, axis=1)}")
print(f"Media lungo le colonne: {np.mean(arr_2d, axis=0)}")

# Generazione di array con np.arange e np.linspace
print("Generazione di array con arange e linspace:")
arr_arange = np.arange(0, 10, 2)  # Crea array con numeri da 0 a 10 con passo 2
print(f"Array con np.arange(0, 10, 2): {arr_arange}")
arr_linspace = np.linspace(0, 1, 5)  # Crea 5 numeri equidistanti tra 0 e 1
print(f"Array con np.linspace(0, 1, 5): {arr_linspace}")

# Creazione di array di zeri, uno e identità
print("Creazione di array speciali:")
zeros_arr = np.zeros((3, 3))  # Array 3x3 di zeri
print(f"Array di zeri (3x3):\n{zeros_arr}")
ones_arr = np.ones((2, 4))  # Array 2x4 di uno
print(f"Array di uni (2x4):\n{ones_arr}")
identity_arr = np.eye(4)  # Matrice identità 4x4
print(f"Matrice identità (4x4):\n{identity_arr}")

# Condizioni booleane su array
print("Operazioni con condizioni booleane:")
bool_mask = arr > 30  # Maschera booleana
print(f"Maschera booleana per arr > 30: {bool_mask}")
filtered_arr = arr[arr > 30]  # Elementi che soddisfano la condizione
print(f"Elementi di arr maggiori di 30: {filtered_arr}")

# Operazioni random
print("Operazioni con numeri casuali:")
random_arr = np.random.rand(3, 3)  # Array 3x3 di numeri casuali uniformi tra 0 e 1
print(f"Array di numeri casuali:\n{random_arr}")
random_int_arr = np.random.randint(0, 100, (4, 4))  # Array 4x4 di interi casuali tra 0 e 100
print(f"Array di interi casuali:\n{random_int_arr}")