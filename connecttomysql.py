import pandas as pd
import mysql.connector
# in mysql connector " ; " is not required at the end of every query 
from mysql.connector import pooling
# Instead of creating new connections repeatedly, a pool of reusable connections is maintained.
# Create a connection pool
db_pool = pooling.MySQLConnectionPool( 
    pool_name="pool1",
    host="localhost",      # MySQL server location
    user="root",           # MySQL username
    password="faizankhan@", # mysql password 
    port=3306        ,     # MySQL port number
    database = "faizan" ,   # selects the database
    connection_timeout=10  , # wait 10 seconds
    charset="utf8mb4",    # characcter offset used for adding emoji and other text 
    ssl_disabled=False     # Controls SSL encryption for the database connection.  False maens SSL encryption enabled , True means SSL disabled
)
# Get a connection from the pool
conn = db_pool.get_connection()
# Create cursor
cursor = conn.cursor(dictionary=True , buffered=True)
# Execute query
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
# Print results
print("select from student :")
for row in rows:
    print(row)
# execte many commands 
query = "INSERT INTO student (rolll,name,marks) VALUES (%s,%s,%s)"
data = [
(13,"L",80),
(14,"M",75),
(15,"N",65) ]
try : 
    cursor.executemany(query, data) 
    conn.commit()
except : 
    conn.rollback()
cursor.execute("SELECT * FROM student")
# Fetch all rows returned by a SELECT query.
rows = cursor.fetchall()
# print result 
print("select from student :")
for r in rows:
    print(r)
# fetch required rows 
print("the required rows : ")
rows = cursor.fetchmany(3)
# print result 
for r in rows:
    print(r)
cursor.fetchall()
# Returns number of rows affected.
print("the rows affected : ")
cursor.execute("DELETE FROM student WHERE rolll=21")
conn.commit()
print(cursor.rowcount)
# Returns the ID of the last inserted row.
try :
    cursor.execute( "INSERT INTO student VALUES(16,'Z',75)" )
    conn.commit()
except :
    conn.rollback()
print ("the rows affected : ")
print(cursor.lastrowid)
# rollback 
try :
    cursor.execute( "INSERT INTO student VALUES(17,'Z',75)" )
    conn.commit()
except :
    conn.rollback()
# Get column names from query result
print("columns from student1 : ")
cursor.execute("SELECT * FROM student1")
for column in cursor.description:
    print(column[0])
cursor.fetchall()
# call a procedure
a = int(input("enter the number to search "))
print("the called procedure Hii: ") 
cursor.execute("CALL hii(%s)",(a,))
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.nextset()   # clear remaining internal result
# autocommit turning off for manual commit() 
conn.autocommit = False 
# Retrieve database structure information.
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
cursor.fetchall()
# user input
x = int(input("Enter minimum marks: "))
y = input("Enter the tbale in which you want to seach ")
# The f before the string means it is an f-string (formatted string literal) , It allows you to insert variables directly inside a string using {}.
query = f"SELECT * FROM {y} WHERE marks > %s "
cursor.execute(query, (x,))
rows = cursor.fetchall()
for row in rows:
    print(row)
# for single line string we use "xyz" , for multilines string we use """xyz"""
table = input("Enter the name of the tbale to be created : ")
query = f"""
CREATE TABLE IF NOT EXISTS {table} (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)"""
cursor.execute(query)
print(f"The create table {table} command executed  " )
# insert into table testing by excel file and csv 
read = pd.read_csv("student.csv")
print(read.columns)
read = read.drop(columns=["Unnamed: 0"])
query = "INSERT INTO testing (id, name, marks) VALUES (%s,%s,%s)"
data = read.values.tolist()
cursor.executemany(query,data )
conn.commit()
readxl = pd.read_excel("student_marks_100.xlsx")
query = "INSERT INTO testing (id, name, marks) VALUES (%s,%s,%s)"
dataxl = readxl.values.tolist()
cursor.executemany(query,dataxl )
conn.commit()
# Close cursor
cursor.close()
# Return connection to pool
if conn.is_connected():
    conn.close()
    