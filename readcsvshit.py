import pandas as pd

df = pd.read_csv(
    "data.csv",              # filepath_or_buffer: path to the CSV file
    
    sep=",",                 # sep: delimiter (e.g., ',' ';' '\t')
    header=0,                # header: row number to use as column names
    names=["A", "B", "C"],   # names: custom column names
    
    usecols=["A", "B"],      # usecols: read only specific columns
    nrows=100,               # nrows: number of rows to read
    skiprows=1,              # skiprows: skip initial rows
    
    dtype={"A": int},        # dtype: define data types of columns
    parse_dates=["B"],       # parse_dates: convert column(s) to datetime
    
    na_values=["NA", "?"],   # na_values: additional strings to recognize as NaN
    keep_default_na=True,    # keep_default_na: include default NaN values
    
    chunksize=None,          # chunksize: read file in chunks (e.g., 1000 rows at a time)
    low_memory=False,        # low_memory: process file in chunks to reduce memory usage
    
    encoding="utf-8",        # encoding: file encoding type
    on_bad_lines="skip"      # on_bad_lines: handle bad lines ('error', 'warn', 'skip')
)

# Display first few rows
print(df.head())