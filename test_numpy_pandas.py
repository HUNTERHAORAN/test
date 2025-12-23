import numpy as np
import pandas as pd

print("=== Python script start ===")

arr = np.array([1, 2, 3, 4])
print("numpy mean:", arr.mean())

df = pd.DataFrame({
    "a": [10, 20, 30],
    "b": [1.1, 2.2, 3.3]
})
print("pandas dataframe:")
print(df)

print("=== Python script end ===")
