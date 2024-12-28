#2. From Python code we are creating a database – python1db
import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',
                               password='1234')

if conn.is_connected():
    print('connection established')
# print(conn)

mycursor = conn.cursor()
mycursor.execute('create database webgui')
print(mycursor)

