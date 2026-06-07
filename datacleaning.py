import pandas as pd
import numpy as np
falsy_values = (0, False, None, '', [], {})
# none become nan in numeriec columns (A) and remains none in object columns (B)
df = pd.DataFrame({
    "A": [10, 0, None, 5],
    "B": ['', 'Hello', None, 'World'],
    "C": [True, False, True, False]
})
print("Original DataFrame:")
print(df)
print("-" * 40)
df["A_is_falsy"] = df["A"].isin(falsy_values)
df["B_is_falsy"] = df["B"].isin(falsy_values)
print("After checking falsy values:")
print(df)
print("-" * 40)
df_falsy_A = df[df["A"].isin(falsy_values)]
print("Rows where column A is falsy:")
print(df_falsy_A)
print("-" * 40)
df["has_any_falsy"] = df[["A", "B", "C"]].isin(falsy_values).any(axis=1)
print("Rows having any falsy value:")
print(df)
print("-" * 40)
df["A_cleaned"] = df["A"].apply(
    lambda x: "INVALID" if x in falsy_values else x
)
print("After replacing falsy values in column A:")
print(df)
print("-" * 40)
# Filling NaN values in column A with 0
df["A_filled"] = df["A"].fillna(0)
print("After filling NaN values in column A:")
print(df)
print("-" * 40)
print(df["B"].isna())
print(df["A"].isna())
print(df["C"].isna())