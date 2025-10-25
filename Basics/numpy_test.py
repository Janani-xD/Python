import numpy as np
import pandas as pd

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Flatten the array using default (C-order)
flattened_c = arr.flatten()
print("Flattened (C-order):", flattened_c)

# Flatten the array using F-order
flattened_f = arr.flatten(order='F')
print("Flattened (F-order):", flattened_f)

# Demonstrate that flatten returns a copy
flattened_c[0] = 99
print("Modified flattened array:", flattened_c)
print("Original array after modification:", arr)


# import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame({'A': [1, np.nan, 3, 4, np.nan, 6],
                   'B': [10, 20, np.nan, 40, 50, np.nan]})
print(df)
# Perform linear interpolation (default method)
df_interpolated = df.interpolate()
print(df_interpolated)

a = np.array([1, 2])
b = np.array([3, 4])
a1 = np.vstack((a, b))
print(a1)
b1 = np.hstack((a, b))
print(b1)