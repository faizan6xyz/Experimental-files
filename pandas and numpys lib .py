import pandas as pd
import numpy as np
# sereies are 1d labeled array
# dataframe are 2d labeled array
s = pd.Series([85, 90, 78], index=["Faizan", "Aryan", "Kunal"])
print(s)
#iloc is used for position(integer) based indexing , [0:6:2] means from 0 to 6 with step size of 2 and end point is excluded
# loc is used for label based indexing ,  [0:6:2] means from label 0 to label 6 with step size of 2 and end point is included
print(s.iloc[0])
print(s["Aryan"])
print(s.dtypes)
print(s[["Faizan" ,"Kunal"]])
print(s["Faizan":"Kunal"])
print(s[:3])
print(s[s > 89])
print(s[["Faizan" ,"Kunal"]].mean())
print(s[["Faizan" ,"Kunal"]]*100)
print(s[["Faizan" ,"Kunal"]].std())
df = pd.DataFrame({ "Roll": [1, 2, 3, 4, 5, 6],
    "Name": ["Faizan", "Aryan", "Kunal","Faizan1", "Aryan1", "Kunal1"],
    "Marks": [85, 90, 78, 88, 92, 80],
    "Grade": ["A", "A+", "B", "B+", "c" , "c+"] })
print(df)
df.index = ["a", "b", "c", "d", "e", "f"]
print(df)
#head and tail could work without aruguments also
print(df.head(3))
print(df.tail(2))
print(df.dtypes)
print(df["Name"])   
print(df[["Name", "Marks"]])
print(df.columns)
#describe() gives you a quick statistical summary of your data in a DataFrame or Series.
print(df.describe())
print(df.info())
print(df.shape)
print(df.size)
# ndim gives number of dimensions
print(df.ndim)
print(df.values)
print(df.dtypes.value_counts())
# index doesn't change original dataframe unless we use inplace = True
print(df.set_index("Roll"))
print(df.sort_values(by="Marks"))
print(df.sort_values(by="Name"))
# prints rows where marks is greater than 80
print(df[df["Marks"] > 80])
# prints boolean values where condition is met
print(df["Marks"] > 80)
print(df[df["Name"].str.contains("1")])
print(df[df["Name"].str.startswith("F")])
print(df[df["Name"].str.endswith("n")])
# to_frame() converts a Series into a DataFrame
print(df["Name"].to_frame())
print(df["Marks"].mean())
print(df["Marks"].std())
# slicing [1:5] means rows 1 to 4
print(df[1:5])
# slicing [1:5] means rows 1 to 4 with 2 element skip
print(df[1:5:2])
#slicing rows and columns [1;3 , [0,3]] means rows 1 to 2 and columns 0 and 3
print(df.iloc[1:3, [0, 3]])
# slicing rows and columns [1:3 , 1:3] means rows 1 to 2 and columns 1 to 2
print(df.iloc[1:3, 1:3])
# printing rows from a to d 
print(df.loc["a":"d"])
print(df["Marks"] * 10)
print(df["Marks"] + 5)
# for double printing of same column
print(df[["Marks","Marks"]])
# displays rows where Name is Faizan
print(df.loc[df["Grade"]=="B"])
print(df.loc[df["Name"]=="Faizan"])
df.loc[0,"Name"] = "faizannnn"
df.iloc[0, 1] = "faizannnn"
# change the marks 
df.loc[df["Marks"]>90,"Grade"] = "A+"
print(df)
# use alphabetical order for between function thats why aryan isnt printed
print(df.loc[df["Name"].between("Faizan", "Kunal1")])
print(df.loc[df["Name"].str.startswith("Faizan")])
print(df.loc[df["Name"].str.contains("an")])
print(df.loc[df["Name"].isin(["Faizan", "Kunal1"])])
# rename only column headers only , original dataframe remains unchanged unless we use inplace = True
# we cant change index name 
print(df.rename(columns={"Grade": "Gradee", "Marks": "Score"}))
print(df.rename(index={"a": "row1", "b": "row2"}))
print(df.rename(columns={"Name": "Student Name"}))
# plot a table with indes grade and values marks with function mean and max 
print(df.pivot_table(values="Marks", index="Grade", aggfunc="mean"))
print(df.pivot_table(values="Marks", index="Grade", aggfunc="max"))
# Even though Marks itself is numeric, Pandas still tries to compute the mean for all remaining columns in each group. To avoid this warning, we can specify numeric_only=True in the aggregation functions.
# grade uses marks as numberic term for min and max functions . prints max and min marks for each grade
print(df.groupby("Grade").max(numeric_only=True))
print(df.groupby("Grade").min(numeric_only=True))
# printing mean of roll numbers for each marks
print(df.groupby("Marks")[["Roll"]].mean())
# just for grouping count of marks
# size() counts number of occurrences of each unique value in the specified column.
print(df.groupby("Marks").size())
# printing mean of marks for each grade
print(df.groupby("Grade")["Marks"].mean())
# printing mean of roll and marks for each grade
print(df.groupby("Grade")[["Roll", "Marks"]].mean())
# printing mean of roll and max of marks for each grade
print(df.groupby("Grade").agg({"Roll": "mean", "Marks": "max"}))
df["Marks_x2"] = df["Marks"] * 2
df["Marks_plus_10"] = df["Marks"] + 10
df["Marks_plus"] = df["Marks"] + 5
print(df)
# axis =1 means we are dropping a column and axis =0 means dropping a row
# drop works with columns or index only 
# drop doesn't change the df until you type inplace = True
print(df.drop("Marks_x2", axis=1 , inplace=True))
print(df.drop(columns=["Marks_plus_10"]))
print(df.drop("a", axis=0))
print(df.drop(["a","b"], axis=0))
print(df.drop(index=["b"]))
# dropping with going back to df changes original dataframe without inplace = True
df = df.drop(columns=["Marks_plus"])
# np.where(condition, value_if_true, value_if_false) is used to create a new column based on a condition modify the df as we directly go back to df
df['Result'] = np.where(df['Marks'] >= 85, 'Pass', 'Fail')
print(df)
# using lambda function to create a new column based on a condition modify the df as we directly go back to df . map is used when single column is change and apply is used when multiple columns are changed 
df['Result1'] = df['Marks'].map(lambda x: 'Pass' if x >= 80 else 'Fail')
df['Result3'] = df['Marks'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print(df)
# using assign to create a new column based on a condition without going back to df but it doesn't change original dataframe
print(df.assign(Result2=df['Marks'].map(lambda x: 'Pass' if x >= 79 else 'Fail')))
# ignore_index = True is used to reindex the dataframe after appending , it uses new index from 0 to n-1
# appending a new row without going back to df doesnt change original dataframe 
print(pd.concat([df, pd.DataFrame([{  "Roll": 7, "Name": "Rohit", "Marks": 95, "Grade": "A+"}])], ignore_index=True))
# appending a new row with going back to df changes original dataframe
df = pd.concat([df, pd.DataFrame([{  "Roll": 7, "Name": "Rohit", "Marks": 95, "Grade": "A+","Marks_plus_10" : "100" ,"Result" : "pass","Result1" : "pass"}])], ignore_index=True)
print(df)
# loc select rows and column both , but df does only the row , both use boolean indexing
# printing rows where Name is not Faizan , using boolean indexing . then print df[mask] where mask is a boolean series
print(df[df["Name"] != "Faizan"])

#printing rows where Marks is not 90 , , using boolean indexing . then print df[mask] where mask is a boolean series
print(df[df["Marks"] != 90])
# printing name not equal to Faizan using loc 
print(df.loc[df["Name"] != "Faizan"])
# printing rows where Marks is greater than 80
print(df.loc[df["Marks"] > 80])
# printing Grade where Marks is greater than 80
print(df.loc[df["Marks"] > 80 , "Grade"])
# changing all values of a reasult 1 column to bb by not going back to df , doesn't change df
print(df.assign(Result1="bb"))
# changing all values of a reasult 1 column to bbb by directly going back to df , changes df
df["Result1"] = "bbb"
print(df)
df.loc[0:6:2, "Result1"] = "aaa"
print(df)
df.iloc[0:3, df.columns.get_loc("Result1")] = "ccc"
print(df)
print(df.columns.get_loc("Result1") )
print(df.loc[1])
print(df.iloc[1])
# works to drop rows when the marks was index print(df.drop(df[df["Marks"] < 40].index, inplace=True))
print(df)
df = df.drop(df[df["Marks"] < 90].index)
print(df)
# shows the duplicate values 
df = df.duplicated()
# show the duplicate value rows
df = df[df.duplicated()]
df = df.drop_duplicates()
# drop_duplicates() is used to drop duplicate values
# value_counts() counts the number of appearence 
# removes the index while saving the file 
df.to_csv("xxxxxxxxxxx.csv",index=False)
#convert series to frame 
ss = s.to_frame()
sss = pd.DataFrame(s)
 # merge two columns into one 
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})
X = df[["A", "B"]]  
# merge two dataframe 
df1 = pd.DataFrame({"A": [1, 2]})
df2 = pd.DataFrame({"B": [3, 4]})
merged = pd.concat([df1, df2], axis=1)