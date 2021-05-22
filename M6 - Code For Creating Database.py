#This file is used to create the SQL database, table and inserting values into it

import sqlite3

connection = sqlite3.connect("BookStore.db") #Connecting to database
cur = connection.cursor() #Cursor object

#SQL command to create 'books' table
create_table = '''CREATE TABLE books(
    title      TEXT   NOT NULL,
    author     TEXT   NOT NULL,
    price      FLOAT  NOT NULL
);'''

cur.execute(create_table) #Creating 'books' table

#Adding 7 books into the table, you can add more if you want
cur.execute("INSERT INTO books VALUES('Think Python','Allen B. Downey',475);")
cur.execute("INSERT INTO books VALUES('Dive Into Python','Mark Pilgrim',699);")
cur.execute("INSERT INTO books VALUES('Harry Potter','J. K. Rowling',2616);")
cur.execute("INSERT INTO books VALUES('Wings of Fire','A. P. J. Abdul Kalam',262);")
cur.execute("INSERT INTO books VALUES('War and Peace','Leo Tolstoy',2099);")
cur.execute("INSERT INTO books VALUES('Gitanjali','Rabindranath Tagore',395);")
cur.execute("INSERT INTO books VALUES('Feluda Samagra','Satyajit Ray',995);")

connection.commit()  #Saving changes
print("Database created with given values!")

connection.close()   #Closing database connection
