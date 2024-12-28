# 4. Creating tables/show tables
import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='1234',database='webgui')

mycursor = conn.cursor()
#mycursor.execute('create table student(name varchar(50),branch varchar(10), id int)')
#mycursor.execute('create table registration(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, course VARCHAR(100) NOT NULL,fee DECIMAL(10,2) NOT NULL)')


mycursor.execute('Show tables')

for x in mycursor:
    print(x)