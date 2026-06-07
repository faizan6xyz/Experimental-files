import pandas as pd
import numpy as np
df = pd.read_csv("eg1newlysaved.csv")
dfbackup = df.copy()
print(df)
print("name with higer r1 than 10")
df1 = df[(df["R1"] >= 10) & (df["R1"] < 15)]
print(df1)
print("dropping rows with r1 less than 10")
df = df[df["R1"] < 10]
print(df)
# pd.merge(df1, df2, on="ID", how="inner") keeps only common rows
# pd.merge(df1, df2, on="ID", how="outer") keeps all rows
# pd.merge(df1, df2, on="ID", how="left") keeps all rows from left df
# pd.merge(df1, df2, on="ID", how="right") keeps all rows from right df
mergedfs = pd.merge(df1, df, on="Namw", how="outer")
print("merged dataframe")
print(mergedfs)
# Wherever R1_x is NaN in mergedfs , it fills those missing values using the corresponding values from R1_y
mergedfs["R1"] = mergedfs["R1_x"].fillna(mergedfs["R1_y"])
mergedfs = mergedfs.drop(columns=["R1_x", "R1_y"])
print(mergedfs)
df = dfbackup.copy()
print("original dataframe recoverd from backup")
print(df)
# print only those rows from mergedfs where A1_x is not NaN
print("rows from mergedfs where A1_x is not NaN")
# notna() Returns True where value is NOT NaN, otherwise False and isna() returns True where value is NaN, otherwise False
print(mergedfs[mergedfs["A1_x"].notna()])
print(mergedfs[mergedfs["A1_x"].notna()]["R1"])
print(mergedfs.loc[mergedfs["A1_x"].notna() ,"R1"])
# dropping all rows where A1_x is NaN
mergedfs = mergedfs.dropna(subset=["A1_x"])
# filling all NaN values in A1_x column with 2
mergedfs["A1_x"] = mergedfs["A1_x"].fillna(2)
# find index of first NaN in A1_x column and set its value in A1_y column to 2 , idxmax() returns index of first occurrence of maximum value
idx = mergedfs["A1_y"].isna().idxmax()
mergedfs.loc[idx, "A1_y"] = 2
# find all indices where A1_x is NaN and set their values in A1_x column to 2
nan_rows = mergedfs[mergedfs["A1_y"].isna()].index
mergedfs.loc[nan_rows, "A1_y"] = 2
# directly setting value at index 2 of A1_y column to 2
mergedfs.loc[2, "A1_y"] = 2
print(mergedfs)
print(mergedfs["A1_y"].mean())
print(mergedfs["A1_y"].median())
print(mergedfs["A1_y"].head(4).mean())
print(df[df["Namw"].str.startswith("F")])
print(df[df["Namw"].str.endswith("n")])
print(df[df["Namw"].str.contains("ee")])
df = df.rename(columns={"Namw": "Name"})
df.loc[3, "Name"] = "Faizan khan"
df["new"] = "faizan khan"
print(df)
df[["First", "Last"]] = df["new"].str.split(" ", expand=True)
print(df)
df["quality"] = np.where(df["R1"] > 10, "Good", "Bad")
print(df)
print(mergedfs)