import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("eg.csv")
print(df.columns)
df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
df = df[df["Year"] >= 2021]
print(df)
# keeping only those rows where Industry_code_NZSIOC is 99999 df = df[df["Industry_code_NZSIOC"] == "99999"]
df["Value"] = pd.to_numeric(df["Value"], errors='coerce')
df = df[(df["Value"] < 100) & (df["Value"] > 0)]
print(df.dtypes)
print(df)
df = df[["Value","Year"]]
arr1 = np.array(["2024","2023","2022","2021"],dtype="str")
arr = np.array([0,0,0,0], dtype="float64")
arr[0] = df[df["Year"] == 2024]["Value"].mean()
arr[1] = df[df["Year"] == 2023]["Value"].mean()
arr[2] = df[df["Year"] == 2022]["Value"].mean()
arr[3] = df[df["Year"] == 2021]["Value"].mean()
print(arr)
print(arr1)
plt.bar(arr,arr1)
plt.xlabel("mean ")
plt.ylabel("year")
plt.title("Bar Plot")
plt.show()
# gets the values of Year column without repeating
# yearelement is not a dataframe its a numpy array
yearelements = df["Year"].unique()
print(yearelements)
print(yearelements.dtype)
# group the values as per years . we can us apply(list) or agg(list) , agg(list) is faster 
# here apply(list) “For each group, collect all values and put them into a Python list.”. agg(list) means aggregate the values
yearvalues = df.groupby("Year")["Value"] # yearvalue is not a dataframe , yearvalue is a SeriesGroupBy object.
yearvaluesdfgroupby = df.groupby("Year")[["Value"]] # its a dataframegroupby object
yearvaluesmean = df.groupby("Year")["Value"].mean() # yearvaluemean is series , not a dataframe
yearvaluesmean1 = df.groupby("Year")["Value"].mean() # yearvaluemean1 is series , not a dataframe
yearvaluesdfgroupby1 = df.groupby("Year")# its a dataframegroupby object
print(yearvalues.max())
print(yearvaluesdfgroupby.max())
print(yearvalues.max())
print(yearvalues.apply(list))
print(yearvalues.agg(list))
print(yearvalues.agg(["mean", "min", "max"]))
print(type(yearvalues))
print(type(yearvalues))
print(type(yearvaluesdfgroupby))
print(type(yearvaluesdfgroupby1))
# how to convert yearvaluesdfgroupby into dataframe 
yearvaluesdfgroupby = yearvaluesdfgroupby.mean()
print(type(yearvaluesdfgroupby))
# how to convert yearvaluesmean into dataframe 
yearvaluesmean = yearvaluesmean.to_frame() # works for series ,  not for seriesgroupbyobject and dataframebyobject
yearvaluesmean = yearvaluesmean.reset_index() # works for series ,  not for seriesgroupbyobject and dataframebyobject
print(type(yearvaluesmean))
yearelementscount = df.groupby("Year").count() # its a dataframe 
yearelementscount1 = df.groupby("Year")["Year"].count() # its a series
yearelementscount4 = df.groupby("Year")[["Year"]].count() # its a dataframe
yearelementscount2 = df["Year"].value_counts() # its a series
yearelementscount5 = df["Year"].value_counts().to_frame() # its a dataframe
yearelementscount6 = df["Year"].value_counts().reset_index() # its a dataframe
yearelementscount3 = df.groupby("Year").size()# its a series
yearelementscount7 = df.groupby("Year").size().to_frame()# its a dataframe
yearelementscount8 = df.groupby("Year").size().reset_index()# its a dataframe
print(yearelementscount, "\n",yearelementscount1, "\n",yearelementscount2, "\n",yearelementscount3, "\n",yearelementscount4, "\n",yearelementscount5, "\n",yearelementscount6, "\n",yearelementscount7, "\n",yearelementscount8)
print(type(yearelementscount), "\n",type(yearelementscount1), "\n",type(yearelementscount2), "\n",type(yearelementscount3), "\n",type(yearelementscount4), "\n",type(yearelementscount5), "\n",type(yearelementscount6), "\n",type(yearelementscount7), "\n",type(yearelementscount8))
# deletion of null (nan ) value 
df = df.dropna()
df = df.drop(df[df["Year"] == 2021].index)
df = df[df["Year"] != 2021]
print(df)
# removes the index while saving the file 
df.to_csv("xxxxxxxxxxx.csv",index=False)