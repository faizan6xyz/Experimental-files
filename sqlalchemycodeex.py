
from sqlalchemy import create_engine, Column , Integer, String , text , Inspector , MetaData, Table, delete , insert
# declarative_base() → base class for tables , sessionmaker() → manages database transactions
from sqlalchemy.orm import declarative_base, sessionmaker , session
# create database connection
engine = create_engine( "mysql+mysqlconnector://root:faizankhan%40@localhost/hello" )
metadata = MetaData()
# base class for table models
Base = declarative_base()
# inspect the ingine 
inspect = Inspector(engine)
# create session (sessionmaker prepares a template for creating sessions It connects that template to your database engine)
Session = sessionmaker(bind=engine)
# this object is used to: insert , update , delete , query data
session = Session()

while True :
    option = input("what would you like to do : ")
    if option == "insert" :
        tables_list = inspect.get_table_names()
        tablecount = len(tables_list)
        tablename = input("enter the table name : ")
        exist = 0 
        for i in range(tablecount) :
            if tables_list[i] == tablename :
                exist = 1
        if exist == 1:
            from sqlalchemy.ext.automap import automap_base
            AutoBase = automap_base()
            AutoBase.prepare(engine, reflect=True)
            Student = AutoBase.classes[tablename]
        if exist == 0 :
            colinput = []
            colinputt = []
            print("table doesn't exist .")
            createtable = input("would you like to create table : ")
            if createtable == "yes" :
                sizetable = int(input("enter the number of columns in tbale : "))
                print("""column type : for integer give input = "Integer" , for string , intput = "String(50)" """)
                for i in range(sizetable):
                    colname = input(f"write the {i+1} column name : ")
                    coltype = input(f"write the {i+1} column type : ")
                    colinput.append(colname)
                    colinputt.append(coltype)
            class Student(Base):
                __tablename__ = tablename
                # orm require primary key to work , by default for integer it has auto increment and initialization 
                pk = Column(Integer,primary_key=True)
            for i in range(sizetable): 
                if colinputt[i] == "int":
                    dtype = Integer
                if colinputt[i]== "string":
                    dtype = String(50)
                setattr(Student, colinput[i], Column(dtype))
        # create table in database , create a table if not exist 
        Base.metadata.create_all(engine)
        # columns from the table 
        columns = inspect.get_columns(tablename)
        for col in columns:
            print(col["name"], col["type"])
            
        #antoher way of getting column  
        '''result = session.execute(text(f"describe {tablename}"))
        for row in result:
            print(row)'''
        

        chint = int(input("how many rows you need to insert "))
        chincol = int(input("how many columns you want to insert "))
        insert = []
        chinput = []
        for i in range(chincol):
            dd = input(f"name {i+1} the column : ")
            insert.append(dd)
        for i in range(chint):
            x = 0 
            for j in  range(chincol): 
                cc = input(f"enter the data for the column {insert[j]} :") 
                chinput.append(cc)
            data = dict(zip(insert, chinput))
            s1 = Student(**data)
            try :
                session.add(s1)
                session.commit()
                print("Row inserted:", data)
            except : 
                session.rollback()
                print("cant be inserted")
            chinput.clear()
            data.clear()
        print("insertion successful ")
    # fetch data 
        '''result = session.execute(text(f"select * from {tablename}"))
        for row in result:
            print(row)'''
    # fetch data 2.0
        students = session.query(Student).all()
        for s in students:
            for c in columns:
                print(getattr(s, c["name"]), end=" ")
            print()


        #insert 2.0 suing traditional method
    '''
        studentinsert = Table( tablename , metadata, autoload_with=engine )
        stmtt = insert(studentinsert).values(**data)
        with engine.connect() as conn:
            conn.execute(stmtt)
            conn.commit()
        '''
    if option == "delete" :
        # deletion part
        tablename = input("enter the table name : ")
        y = input("Enter the column which has reference to delete : ")
        x = int(input("Enter the column element where the deletion should take place : "))
        # table defineing 
        studentdelete = Table(
            tablename,
            metadata,
            autoload_with=engine
        )
        # delete statement
        stmt = delete(studentdelete).where(studentdelete.c[y] == x)
        # execute
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
        result = session.execute(text(f"select * from {tablename}"))
        for row in result:
            print(row)
        print("deletion sucessfull")
    if option == "exit":
        break 
    else :
        print("enter the right operation ")
    