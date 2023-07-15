# Question 1

# Answer 1 - Database is the collection of organized data that is structured or unstructured.
# The database's primary goal is to store a huge amount of data.
# Difference between SQL & NOSQL databases is that SQL databases store structured datasets in row & column formats
# whereas NOSQL databases stored unstructured datasets such as audio, video, images, etc.

# Question 2

# Answer 2 - DDL stands for Data Definition Language. 
# Data Definition Language actually consists of the SQL commands that can be used to define the database schema.
# It simply deals with descriptions of the database schema and is used to create and modify the structure of database
# objects in the database. DDL is a set of SQL commands used to create, modify, and delete database structures but not data.
# These commands are normally not used by a general user, who should be accessing the database via an application
# List of DDL commands: -
# 1. CREATE: This command is used to create the database or its objects
#    (like table, index, function, views, store procedure, and triggers).
# 2. DROP: This command is used to delete objects from the database.
# 3. ALTER: This is used to alter the structure of the database.
# 4. TRUNCATE: This is used to remove all records from a table, including all spaces allocated for the records are removed.

# example of the above 4 commands: -

# 1. Create command example
import mysql.connector

#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))")
mycursor.execute("CREATE TABLE if not exists test1.test_table1(c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))")

# 2. Alter command example

mycursor.execute("ALTER TABLE test1.test_table1 MODIFY c4 VARCHAR(40)")
mycursor.execute("ALTER TABLE test1.test_table1 MODIFY c5 VARCHAR(40)")

# 3. Truncate command example
mycursor.execute("insert into  test1.test_table values(3424,'abc',123,56.56,'xyz') ")
mycursor.execute("insert into  test1.test_table values(3424,'abc',123,56.56,'xyz') ")
mycursor.execute("insert into  test1.test_table values(3424,'abc',123,56.56,'xyz') ")
mydb.commit()



mycursor.execute("TRUNCATE TABLE test1.test_table")


# 4. Drop command example
mycursor.execute("DROP TABLE if exists test1.test_table1")


# Question 3

# Answer 3 - DML stands for Data Manipulation Language.
# The SQL commands that deal with the manipulation of data present in the database belong to DML
# or Data Manipulation Language and this includes most of the SQL statements.
# It is the component of the SQL statement that controls access to data and to the database.

# List of DML commands: 

# 1. INSERT: It is used to insert data into a table.
# 2. UPDATE: It is used to update existing data within a table.
# 3. DELETE: It is used to delete records from a database table.

# example of the above 3 commands: -

# 1. Insert command example

mycursor.execute("insert into  test1.test_table values(1234,'abc',123,56.56,'xyz') ")
mycursor.execute("insert into  test1.test_table values(4567,'abc',123,56.56,'xyz') ")
mycursor.execute("insert into  test1.test_table values(7890,'abc',123,56.56,'xyz') ")
mydb.commit()

# 2. Update command example

mycursor.execute("update test1.test_table set c2='pwskills'where c1=1234 ")
mydb.commit()

# 3. Delete command example

mycursor.execute("Delete from test1.test_table where c1=4567 ")
mydb.commit()

# Question 4

# Answer 4 - DQL stands for Data Query Language.
# DQL statements are used for performing queries on the data within schema objects. 
# The purpose of the DQL Command is to get some schema relation based on the query passed to it. 
# We can define DQL as follows it is a component of SQL statement that allows getting data from the database 
# and imposing order upon it.

# List of DQL: 

# SELECT: It is used to retrieve data from the database.

# 1. Select command example

mycursor.execute("select * from test1.test_table ")

for i in mycursor.fetchall():
    print (i)

mydb.close()
# Question 5

# Answer 5 - A primary key is used to ensure data in the specific column is unique.
# A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables.
# It uniquely identifies a record in the relational database table

# Question 6

# Answer 6 Python code to connect MySQL to Python

import mysql.connector

#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()

# Cursor method - Allows Python code to execute PostgreSQL command in a database session.
# Cursors are created by the connection. 
# cursor() method: they are bound to the connection for the entire lifetime and all the commands 
# are executed in the context of the database session wrapped by the connection.

# Execute method - This method executes the given database operation (query or command).

# Question 7 - 

# Answer 7 - order of execution of SQL clauses in an SQL query.

# 1. From - Tables are joined to get the base data.
# 2. Where - The base data is filtered.
# 3. Group by - The filtered base data is grouped.
# 4. Having - The grouped base data is filtered.
# 5. Select - The final data is returned.
# 6. Order by - The final data is sorted.
# 7. Limit - The returned data is limited to row count.
