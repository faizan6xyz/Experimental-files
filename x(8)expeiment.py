import pandas as pd
import numpy as np
df = pd.read_csv("x (8).csv")
print(df.columns)
df = df.sort_values("Data_value")
print(df)
df = df.dropna(subset=["Data_value"]) # drop Nan values of Data-value column
df = df[df["Data_value"].notna()] # selects non Nan vlaues of Data-value column
df = df.drop(columns=["Series_title_2"]) # cause series "Series_title_2" have all the rows NAN
df = df.dropna() # drop every row with NaN
print(df)
print(df.isna().sum()) # show's each column's the sum of NaN 
print(df.isna().sum().sum()) # show the sum of NaN of  df
df["Period"] = pd.to_numeric(df["Period"])
df = df[df["Period"]>2010.00]
df = df.tail(100)
uno = df["Series_title_1"].unique()
print(uno)
df["Group"] = df["Group"].astype("string")
unoo = df["Group"].unique()
print(unoo)
xx = df[df["Group"].str.contains("Level 2")]
xxx = df[df["Group"].str.contains("Level 3")]
x = df[df["Group"].str.contains("Level 1")]
print(x)
print(type(x))
print(xx)
print(type(xx))
print(xxx)
print(type(xxx))
fd = pd.read_excel("xx.xlsx")
print(fd)
fd1 = pd.read_excel("x.xlsx")
print(fd1)
fd2 = pd.read_excel("Project-Management-Sample-Data.xlsx")
print(fd2)
print(fd2.columns)
fd2 = fd2.drop(columns="Unnamed: 0")
fd2 = fd2.rename(columns={"Unnamed: 1" : "Project name" ,"Unnamed: 2" : "Take name" ,"Unnamed: 3" : "Assigned to" ,"Unnamed: 4" : "Start date" ,"Unnamed: 5" : "Days required" ,"Unnamed: 6" : "End date" , "Unnamed: 7" : "Progress" })
print(fd2.columns)
fd2copy = fd2.copy()
fd2 = fd2.dropna()
print(fd2)
fd2 = fd2.reset_index()
print(fd2)
fd2 = fd2.drop(columns="index")
print(fd2)
print(fd2.index)
fd2 = fd2.drop(fd2.index[0])
fd2 = fd2.drop(index=1)
print(fd2)
print(fd2.dtypes)
fd2["Days required"] = pd.to_numeric(fd2["Days required"])
fd2["Start date"] = pd.to_datetime(fd2["Start date"])
fd2["End date"] = pd.to_datetime(fd2["End date"])
print(fd2.dtypes)
print(fd2)
# computers and Python usually store percentages as fractions (ratios), not as “percent values.”
fd2 = fd2[fd2["Progress"]== 1]
print(fd2)
fd2["Progress"] = fd2["Progress"]*100
fd2 = fd2.sort_values(by = "Days required")
print(fd2)
fd2 = fd2.head(3)
print(fd2)
print(fd2["Assigned to"])
df1 = pd.read_excel("fsi-2021.xlsx")
print(df1)
print(df1.dtypes)
print(df1.columns)
df1 = df1.dropna()
df1EconomicInequality = df1.sort_values(by="E2: Economic Inequality",ascending=False)
print(df1EconomicInequality)
df1EconomicInequality = df1EconomicInequality.head(10)
df1EconomicInequality = df1EconomicInequality["E2: Economic Inequality"]
print(df1EconomicInequality)
print(type(df1EconomicInequality))
print(fd2)
xx =  pd.read_csv("x (8).csv")
# its dataframe  now and then convert into series
xx = xx[["Series_reference","Period"]]
# or xx = pd.read_csv("x (8).csv", usecols=['Series_reference','period'])
print(xx)
# its series now converted by dataframe 
xx = xx["Series_reference"]
# or xx =  pd.read_csv("x (8).csv", usecols = ["Series_reference"])
print(xx)
# dataframe could be converted into series but series couldn't be converted into dataframe 