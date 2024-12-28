# 1.Connecting to the MySQL database (Connect MySQL database using MySQL-Connector Python)

# 1st type of making connection
import mysql.connector

#Connecting to the server
conn = mysql.connector.connect(host = 'localhost',user = 'root', password = '1234')

if conn.is_connected():
    print("Connection established")
print(conn)


# 2nd way to create a connection
# from mysql.connector import connection

# conn = connection.MySQLConnection(host = 'localhost',user = 'root', password = 'Sunitha@58')

# if conn.is_connected():
#     print("Con es")
# print(conn)



# 3rd way to create a connection using dictionary
#using dictionaries
# from mysql.connector import connection

# dict = {
#         'host' : 'localhost',
#         'user' : 'root', 
#         'password' : 'Sunitha@58'
#         }

# conn = connection.MySQLConnection(**dict)

# print(conn)

#conn.close()