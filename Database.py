"""
To connect to mysql first download and install my-sql connector
then open a connection and using cursor method connect and perform crud operations
"""

import mysql.connector

mydb = mysql.connector.connect(user = 'root',
                               password = 'Saturn12$',
                               host = 'localhost',
                               database = 'telusko')

mycursor = mydb.cursor()

mycursor.execute('select * from student')

for result in mycursor:
    print(result)