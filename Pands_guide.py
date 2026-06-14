"""
================================================================================
  PANDAS — COMPLETE ADVANCED REFERENCE
  Covers: Series, DataFrame, Indexing, Cleaning, GroupBy, Merge, Pivot,
          Time Series, Apply, MultiIndex, IO, Visualization, Performance
================================================================================
"""

import pandas as pd
import numpy as np


# 1. SERIES — 1D labeled array
def series_basics():
    print("\n--- 1. SERIES ---")

    # create
    s = pd.Series([10, 20, 30, 40])
    print(s)

    # with custom index
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print(s["b"])          # 20

    # from dict
    s = pd.Series({"x": 1, "y": 2, "z": 3})

    # attributes
    print(s.values)        # numpy array
    print(s.index)         # Index object
    print(s.dtype)
    print(s.shape)
    print(s.size)

    # operations
    print(s * 2)
    print(s[s > 1])        # filter
    print(s.sum(), s.mean(), s.max(), s.min(), s.std())

    # vectorized string ops
    s = pd.Series(["Alice", "Bob", "Charlie"])
    print(s.str.lower())
    print(s.str.contains("li"))
    print(s.str.len())


# 2. DATAFRAME — 2D labeled table
def dataframe_basics():
    print("\n--- 2. DATAFRAME ---")

    # from dict
    df = pd.DataFrame({
        "name":   ["Alice", "Bob", "Charlie", "David", "Eve"],
        "age":    [25, 30, 35, 28, 22],
        "salary": [50000, 60000, 75000, 55000, 48000],
        "dept":   ["HR", "IT", "IT", "HR", "Finance"],
        "city":   ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai"],
    })

    # from list of dicts
    df2 = pd.DataFrame([
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
    ])

    # from numpy array
    df3 = pd.DataFrame(np.random.randn(4, 3), columns=["A", "B", "C"])

    # basic info
    print(df.head(3))
    print(df.tail(2))
    print(df.shape)          # (rows, cols)
    print(df.columns.tolist())
    print(df.dtypes)
    print(df.info())
    print(df.describe())     # stats summary

    return df


# 3. INDEXING & SELECTION
def indexing(df):
    print("\n--- 3. INDEXING & SELECTION ---")

    # select column
    print(df["name"])
    print(df[["name", "salary"]])

    # loc — label based
    print(df.loc[0])                          # row 0
    print(df.loc[0:2, "name":"salary"])       # rows 0-2, cols name to salary
    print(df.loc[df["age"] > 27])             # filter rows

    # iloc — position based
    print(df.iloc[0])                         # first row
    print(df.iloc[0:3, 0:2])                 # first 3 rows, first 2 cols
    print(df.iloc[-1])                        # last row

    # at / iat — single value (faster)
    print(df.at[0, "name"])                   # label
    print(df.iat[0, 0])                       # position

    # boolean filtering
    print(df[df["salary"] > 55000])
    print(df[(df["dept"] == "IT") & (df["age"] < 33)])
    print(df[df["city"].isin(["Delhi", "Mumbai"])])

    # query string (cleaner syntax)
    print(df.query("salary > 55000 and dept == 'IT'"))

    # set index
    df2 = df.set_index("name")
    print(df2.loc["Alice"])
    df2 = df2.reset_index()


# 4. DATA CLEANING
def data_cleaning():
    print("\n--- 4. DATA CLEANING ---")

    df = pd.DataFrame({
        "name":   ["Alice", "Bob", None, "David", "Eve"],
        "age":    [25, None, 35, 28, 22],
        "salary": [50000, 60000, 75000, None, 48000],
        "dept":   ["HR", "IT", "IT", "HR", "  Finance  "],
        "score":  [88, 92, 88, 75, 92],
    })

    # detect nulls
    print(df.isnull())
    print(df.isnull().sum())       # count nulls per column
    print(df.isnull().any())       # which columns have nulls

    # drop nulls
    df.dropna()                    # drop rows with any null
    df.dropna(subset=["age"])      # drop only where age is null
    df.dropna(axis=1)              # drop columns with any null
    df.dropna(thresh=3)            # keep rows with at least 3 non-null

    # fill nulls
    df["age"].fillna(df["age"].mean(), inplace=True)
    df["salary"].fillna(df["salary"].median(), inplace=True)
    df["name"].fillna("Unknown", inplace=True)
    df.ffill()                     # forward fill
    df.bfill()                     # backward fill

    # duplicates
    print(df.duplicated())
    print(df.duplicated(subset=["score"]))
    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset=["score"], keep="first", inplace=True)

    # string cleaning
    df["dept"] = df["dept"].str.strip()
    df["dept"] = df["dept"].str.lower()
    df["dept"] = df["dept"].str.replace("hr", "Human Resources")
    df["name"] = df["name"].str.title()

    # type conversion
    df["age"] = df["age"].astype(int)
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    # rename columns
    df.rename(columns={"dept": "department", "score": "test_score"}, inplace=True)

    # drop columns
    df.drop(columns=["test_score"], inplace=True)

    # replace values
    df["department"].replace("Human Resources", "HR", inplace=True)

    print(df)
    return df


# 5. ADDING / MODIFYING COLUMNS
def column_operations(df):
    print("\n--- 5. COLUMN OPERATIONS ---")

    df = df.copy()

    # add new column
    df["bonus"]        = df["salary"] * 0.10
    df["senior"]       = df["age"] > 30
    df["name_upper"]   = df["name"].str.upper()
    df["salary_band"]  = pd.cut(df["salary"],
                                bins=[0, 50000, 65000, 100000],
                                labels=["Low", "Mid", "High"])

    # insert at specific position
    df.insert(1, "emp_id", range(1, len(df) + 1))

    # conditional column
    df["level"] = np.where(df["salary"] > 60000, "Senior", "Junior")

    # multiple conditions
    conditions  = [df["salary"] < 50000, df["salary"] < 65000, df["salary"] >= 65000]
    choices     = ["Low", "Mid", "High"]
    df["band2"] = np.select(conditions, choices)

    print(df.head())
    return df


# 6. SORTING
def sorting(df):
    print("\n--- 6. SORTING ---")

    print(df.sort_values("salary", ascending=False))
    print(df.sort_values(["dept", "salary"], ascending=[True, False]))
    print(df.sort_index())

    # rank
    df["salary_rank"] = df["salary"].rank(ascending=False)
    print(df[["name", "salary", "salary_rank"]])


# 7. GROUPBY
def groupby_ops(df):
    print("\n--- 7. GROUPBY ---")

    # basic aggregation
    print(df.groupby("dept")["salary"].mean())
    print(df.groupby("dept")["salary"].sum())
    print(df.groupby("dept")["salary"].agg(["mean", "min", "max", "count"]))

    # multiple columns
    print(df.groupby(["dept", "city"])["salary"].mean())

    # agg with dict — different agg per column
    print(df.groupby("dept").agg({
        "salary": ["mean", "max"],
        "age":    "mean",
        "name":   "count",
    }))

    # transform — returns same shape as original (for adding group stats back)
    df["dept_avg_salary"] = df.groupby("dept")["salary"].transform("mean")
    df["salary_vs_avg"]   = df["salary"] - df["dept_avg_salary"]
    print(df[["name", "dept", "salary", "dept_avg_salary", "salary_vs_avg"]])

    # filter — keep groups that meet condition
    high_paying = df.groupby("dept").filter(lambda g: g["salary"].mean() > 55000)
    print(high_paying)

    # apply — custom function per group
    def top_earner(group):
        return group.nlargest(1, "salary")

    print(df.groupby("dept").apply(top_earner))

    # size / count
    print(df.groupby("dept").size())
    print(df.groupby("dept").count())


# 8. MERGE / JOIN
def merge_join():
    print("\n--- 8. MERGE / JOIN ---")

    employees = pd.DataFrame({
        "emp_id": [1, 2, 3, 4],
        "name":   ["Alice", "Bob", "Charlie", "David"],
        "dept_id":[10, 20, 20, 30],
    })

    departments = pd.DataFrame({
        "dept_id":   [10, 20, 40],
        "dept_name": ["HR", "IT", "Finance"],
    })

    projects = pd.DataFrame({
        "emp_id":   [1, 2, 2, 3],
        "project":  ["P1", "P2", "P3", "P1"],
    })

    # inner join — only matching rows
    print(pd.merge(employees, departments, on="dept_id", how="inner"))

    # left join — all from left, matched from right
    print(pd.merge(employees, departments, on="dept_id", how="left"))

    # right join
    print(pd.merge(employees, departments, on="dept_id", how="right"))

    # outer join — all rows from both
    print(pd.merge(employees, departments, on="dept_id", how="outer"))

    # different column names
    print(pd.merge(employees, departments,
                   left_on="dept_id", right_on="dept_id"))

    # many-to-many
    print(pd.merge(employees, projects, on="emp_id"))

    # join on index
    df1 = employees.set_index("emp_id")
    df2 = projects.set_index("emp_id")
    print(df1.join(df2, how="left"))

    # concat — stack dataframes
    df_top    = employees.iloc[:2]
    df_bottom = employees.iloc[2:]
    print(pd.concat([df_top, df_bottom], ignore_index=True))

    # concat side by side
    print(pd.concat([employees, departments], axis=1))


# 9. PIVOT TABLE & CROSSTAB
def pivot_operations(df):
    print("\n--- 9. PIVOT TABLE & CROSSTAB ---")

    # pivot table
    pivot = pd.pivot_table(
        df,
        values="salary",
        index="dept",
        columns="city",
        aggfunc="mean",
        fill_value=0,
        margins=True,       # adds row/col totals
    )
    print(pivot)

    # crosstab — frequency table
    ct = pd.crosstab(df["dept"], df["city"])
    print(ct)

    # crosstab with normalize
    ct_norm = pd.crosstab(df["dept"], df["city"], normalize="index")
    print(ct_norm)

    # pivot (simple reshape — needs unique index/col pairs)
    simple = pd.DataFrame({
        "date":  ["2024-01", "2024-01", "2024-02", "2024-02"],
        "item":  ["A", "B", "A", "B"],
        "sales": [100, 200, 150, 250],
    })
    print(simple.pivot(index="date", columns="item", values="sales"))

    # melt — unpivot (wide to long)
    wide = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "math": [90, 85],
        "science": [88, 92],
    })
    long = pd.melt(wide, id_vars="name", var_name="subject", value_name="score")
    print(long)


# 10. APPLY, MAP, APPLYMAP
def apply_map(df):
    print("\n--- 10. APPLY / MAP ---")

    df = df.copy()

    # apply on column (Series)
    df["salary_k"] = df["salary"].apply(lambda x: f"{x/1000:.0f}K")

    # apply with custom function
    def classify_age(age):
        if age < 25:   return "Young"
        if age < 32:   return "Mid"
        return "Senior"

    df["age_group"] = df["age"].apply(classify_age)

    # apply on entire row (axis=1)
    df["summary"] = df.apply(
        lambda row: f"{row['name']} earns {row['salary']} in {row['dept']}",
        axis=1
    )

    # apply on entire DataFrame (column-wise by default)
    numeric_cols = df.select_dtypes(include="number")
    print(numeric_cols.apply(lambda col: col.max() - col.min()))

    # map — element-wise on Series (replaces values)
    dept_map = {"HR": "Human Resources", "IT": "Information Technology"}
    df["dept_full"] = df["dept"].map(dept_map)

    # where / mask
    df["capped_salary"] = df["salary"].where(df["salary"] < 70000, 70000)

    print(df[["name", "salary_k", "age_group", "dept_full"]].head())


# 11. STRING OPERATIONS
def string_operations():
    print("\n--- 11. STRING OPERATIONS ---")

    df = pd.DataFrame({
        "name":  ["  alice smith  ", "BOB JONES", "charlie brown"],
        "email": ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com"],
        "phone": ["9876543210", "1234567890", "5555555555"],
    })

    df["name"] = df["name"].str.strip().str.title()
    df["domain"] = df["email"].str.split("@").str[1]
    df["username"] = df["email"].str.split("@").str[0]
    df["is_gmail"] = df["email"].str.contains("gmail")
    df["name_len"] = df["name"].str.len()
    df["first_name"] = df["name"].str.split(" ").str[0]
    df["phone_fmt"] = df["phone"].str.replace(r"(\d{5})(\d{5})", r"\1-\2", regex=True)

    # extract with regex
    df["area_code"] = df["phone"].str.extract(r"(\d{3})")

    print(df)


# 12. TIME SERIES
def time_series():
    print("\n--- 12. TIME SERIES ---")

    # create date range
    dates = pd.date_range(start="2024-01-01", periods=12, freq="ME")  # month end
    df = pd.DataFrame({
        "date":  dates,
        "sales": np.random.randint(1000, 5000, 12),
        "cost":  np.random.randint(500, 2000, 12),
    })

    # parse dates
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")

    # extract date parts
    df["year"]    = df.index.year
    df["month"]   = df.index.month
    df["quarter"] = df.index.quarter
    df["weekday"] = df.index.day_name()

    # resample — like groupby for time
    print(df["sales"].resample("QE").sum())     # quarterly sum
    print(df["sales"].resample("QE").mean())    # quarterly mean

    # rolling — moving window
    df["rolling_avg_3m"] = df["sales"].rolling(window=3).mean()
    df["rolling_sum_3m"] = df["sales"].rolling(window=3).sum()

    # expanding — cumulative
    df["cumulative_sales"] = df["sales"].expanding().sum()

    # shift — lag/lead
    df["prev_month_sales"] = df["sales"].shift(1)
    df["next_month_sales"] = df["sales"].shift(-1)
    df["mom_growth"]       = df["sales"].pct_change() * 100  # month over month %

    # filter by date
    print(df["2024-03":"2024-06"])
    print(df[df.index.month == 1])

    print(df)


# 13. MULTIINDEX
def multiindex():
    print("\n--- 13. MULTIINDEX ---")

    # create multiindex dataframe
    arrays = [
        ["IT", "IT", "HR", "HR"],
        ["Alice", "Bob", "Charlie", "David"],
    ]
    index = pd.MultiIndex.from_arrays(arrays, names=["dept", "name"])
    df = pd.DataFrame({
        "salary": [70000, 65000, 55000, 52000],
        "age":    [30, 28, 35, 29],
    }, index=index)

    print(df)

    # select
    print(df.loc["IT"])                     # all IT rows
    print(df.loc[("IT", "Alice")])          # specific row
    print(df.loc["IT", "salary"])           # IT salary column

    # reset multiindex
    df_reset = df.reset_index()
    print(df_reset)

    # groupby with multiindex result
    df2 = pd.DataFrame({
        "dept":   ["IT", "IT", "HR", "HR"],
        "city":   ["Delhi", "Mumbai", "Delhi", "Mumbai"],
        "salary": [70000, 65000, 55000, 52000],
    })
    multi = df2.groupby(["dept", "city"])["salary"].mean()
    print(multi)
    print(multi.unstack())                  # reshape to wide


# 14. WINDOW FUNCTIONS
def window_functions():
    print("\n--- 14. WINDOW FUNCTIONS ---")

    df = pd.DataFrame({
        "day":   range(1, 11),
        "sales": [100, 120, 90, 150, 110, 130, 95, 160, 140, 125],
    })

    # rolling
    df["roll_mean_3"]  = df["sales"].rolling(3).mean()
    df["roll_max_3"]   = df["sales"].rolling(3).max()
    df["roll_std_3"]   = df["sales"].rolling(3).std()

    # expanding
    df["exp_mean"]     = df["sales"].expanding().mean()
    df["exp_cumsum"]   = df["sales"].expanding().sum()

    # ewm — exponential weighted moving average
    df["ewm_mean"]     = df["sales"].ewm(span=3).mean()

    print(df)


# 15. CATEGORICAL DATA
def categorical():
    print("\n--- 15. CATEGORICAL DATA ---")

    df = pd.DataFrame({
        "grade":  ["A", "B", "C", "A", "B", "D", "C", "A"],
        "score":  [95, 82, 71, 90, 78, 65, 73, 88],
    })

    # convert to category (saves memory, enables ordering)
    df["grade"] = pd.Categorical(
        df["grade"],
        categories=["D", "C", "B", "A"],
        ordered=True
    )

    print(df["grade"].cat.categories)
    print(df["grade"].cat.codes)           # integer codes
    print(df[df["grade"] >= "B"])          # works because ordered=True
    print(df.groupby("grade")["score"].mean())

    # pd.cut — bin numeric into categories
    df["band"] = pd.cut(df["score"],
                        bins=[0, 70, 80, 90, 100],
                        labels=["D", "C", "B", "A"])
    print(df)

    # pd.qcut — quantile-based binning
    df["quartile"] = pd.qcut(df["score"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
    print(df)


# 16. INPUT / OUTPUT — read and write files
def io_operations():
    print("\n--- 16. I/O ---")

    df = pd.DataFrame({
        "name":   ["Alice", "Bob", "Charlie"],
        "salary": [50000, 60000, 75000],
    })

    # CSV
    df.to_csv("output.csv", index=False)
    df_csv = pd.read_csv("output.csv")

    # Excel
    df.to_excel("output.xlsx", index=False, sheet_name="Employees")
    df_excel = pd.read_excel("output.xlsx", sheet_name="Employees")

    # JSON
    df.to_json("output.json", orient="records", indent=2)
    df_json = pd.read_json("output.json")

    # Parquet (fast columnar format — needs pyarrow)
    # df.to_parquet("output.parquet", index=False)
    # df_parquet = pd.read_parquet("output.parquet")

    # read CSV with options
    df2 = pd.read_csv(
        "output.csv",
        usecols=["name"],           # only load specific columns
        dtype={"name": str},        # force dtypes
        na_values=["N/A", "null"],  # treat these as NaN
        skiprows=0,
        nrows=2,                    # read only first 2 rows
    )

    # read in chunks (large files)
    chunk_iter = pd.read_csv("output.csv", chunksize=1)
    for chunk in chunk_iter:
        print(chunk)

    print("I/O done")


# 17. PERFORMANCE & MEMORY
def performance():
    print("\n--- 17. PERFORMANCE & MEMORY ---")

    df = pd.DataFrame({
        "id":     range(100000),
        "value":  np.random.randn(100000),
        "dept":   np.random.choice(["HR", "IT", "Finance"], 100000),
        "active": np.random.choice([True, False], 100000),
    })

    print("Memory before:", df.memory_usage(deep=True).sum() / 1024, "KB")

    # downcast numeric types
    df["id"]    = pd.to_numeric(df["id"], downcast="integer")
    df["value"] = pd.to_numeric(df["value"], downcast="float")

    # convert string columns to category
    df["dept"] = df["dept"].astype("category")

    print("Memory after:", df.memory_usage(deep=True).sum() / 1024, "KB")

    # vectorized ops are faster than apply
    df["value_x2_slow"] = df["value"].apply(lambda x: x * 2)   # slow
    df["value_x2_fast"] = df["value"] * 2                        # fast

    # use query instead of boolean indexing for large frames
    result1 = df[df["dept"] == "IT"]                             # ok
    result2 = df.query("dept == 'IT'")                           # faster on large df

    print(df.dtypes)


# 18. USEFUL UTILITIES
def utilities(df):
    print("\n--- 18. UTILITIES ---")

    # value counts
    print(df["dept"].value_counts())
    print(df["dept"].value_counts(normalize=True))   # proportions

    # unique values
    print(df["dept"].unique())
    print(df["dept"].nunique())

    # sample
    print(df.sample(3))
    print(df.sample(frac=0.4))

    # nlargest / nsmallest
    print(df.nlargest(3, "salary"))
    print(df.nsmallest(2, "age"))

    # correlation
    print(df[["age", "salary"]].corr())

    # cumulative operations
    df["cumsum_salary"] = df["salary"].cumsum()
    df["cumprod"]       = df["salary"].cumprod()
    df["cummax"]        = df["salary"].cummax()

    # clip values
    df["salary_clipped"] = df["salary"].clip(lower=50000, upper=70000)

    # between
    print(df[df["age"].between(25, 30)])

    # isin
    print(df[df["dept"].isin(["IT", "Finance"])])

    # transpose
    print(df.head(2).T)

    # stack / unstack
    stacked = df[["dept", "salary"]].set_index("dept").stack()
    print(stacked)


# 19. PIPE — chain operations cleanly
def pipe_chaining():
    print("\n--- 19. PIPE / METHOD CHAINING ---")

    df = pd.DataFrame({
        "name":   ["Alice", None, "Charlie", "David", "Alice"],
        "dept":   ["HR", "IT", "IT", "HR", "HR"],
        "salary": [50000, 60000, None, 55000, 50000],
        "age":    [25, 30, 35, None, 25],
    })

    def add_bonus(df):
        df["bonus"] = df["salary"] * 0.10
        return df

    def flag_seniors(df):
        df["senior"] = df["age"] > 30
        return df

    result = (
        df
        .dropna(subset=["salary"])
        .drop_duplicates()
        .fillna({"age": df["age"].mean()})
        .rename(columns={"dept": "department"})
        .assign(salary_k=lambda x: x["salary"] / 1000)
        .query("salary > 50000")
        .sort_values("salary", ascending=False)
        .pipe(add_bonus)
        .pipe(flag_seniors)
        .reset_index(drop=True)
    )

    print(result)


# 20. STYLE & DISPLAY
def styling():
    print("\n--- 20. DISPLAY OPTIONS ---")

    # display settings
    pd.set_option("display.max_rows", 100)
    pd.set_option("display.max_columns", 20)
    pd.set_option("display.float_format", "{:.2f}".format)
    pd.set_option("display.width", 120)

    df = pd.DataFrame({
        "name":   ["Alice", "Bob", "Charlie"],
        "salary": [50000.5, 60000.75, 75000.123],
    })

    # style (works in Jupyter)
    styled = (
        df.style
        .highlight_max(subset=["salary"], color="lightgreen")
        .highlight_min(subset=["salary"], color="salmon")
        .format({"salary": "{:,.2f}"})
        .set_caption("Employee Salary Table")
    )

    print(df.to_string(index=False))
    print(df.to_markdown())        # needs tabulate installed


# MAIN
if __name__ == "__main__":
    series_basics()
    df = dataframe_basics()
    indexing(df)
    data_cleaning()
    df = dataframe_basics()       # fresh df for remaining sections
    df = column_operations(df)
    sorting(df)
    groupby_ops(df)
    merge_join()
    pivot_operations(df)
    apply_map(df)
    string_operations()
    time_series()
    multiindex()
    window_functions()
    categorical()
    io_operations()
    performance()
    utilities(df)
    pipe_chaining()
    styling()

    print("\nDone.")