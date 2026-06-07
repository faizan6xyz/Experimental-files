import mysql.connector
conn = mysql.connector.connect(
    host="localhost",      # MySQL server location
    user="root",           # MySQL username
    password="faizankhan@",
    port=3306        ,     # MySQL port number
    database = "hello",
    connection_timeout=10  , # wait 10 seconds
    charset="utf8mb4",    # characcter offset used for adding emoji and other text 
    ssl_disabled=False     # Controls SSL encryption for the database connection.  False maens SSL encryption enabled , True means SSL disabled
)
print("Connected successfully")
# creatign a cursor , cursor allows Python to execute SQL queries. we are using data dictionary to get specific data with information 
cursor = conn.cursor(dictionary=True,buffered=True)
print("you are connnected to database faizan ")
while True :
    insert = input("do you like to insert :")
    if insert == "yes":
        print("tables inside the faizan database :")
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(table)
        cursor.fetchall()
        table = input("name the table ")
        columncount = int(input("how many columns you need to insert "))
        rowinput = int(input("enter the numer of row you want to insert "))
        column = [] 
        print(f"columns in {table} :")
        cursor.execute(f"describe {table}")
        for row in cursor :
            print(row)
        cursor.fetchall()
        # column count is an integer , python doesnt loop through interger
        for i in range(columncount) : 
            col  = input("name the column you want to insert ")
            column.append(col)
        values = []
        for j in range(rowinput): 
            for i in range(columncount):
                value = input(f"Enter value for {column[i]}: ")
                values.append(value)
            # build query  
            cols = ",".join(column)
            placeholders = ",".join(["%s"] * columncount)
            query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
            # insert rows
            cursor.execute(query, values)
            conn.commit()
            values.clear()
        print("\nRows inserted successfully!")
        cursor.execute(f"select * from {table}")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    if insert == "no" : 
        x = input("x")
        cursor.execute(f"select * from {x} ")
        for i in cursor:
            print(i)
        cursor.fetchall() 
        break 
# close the cursor object 
cursor.close()
# Close Connection , Always close the connection when finished.
conn.close()
