# 5. Inserting the records
import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user = 'root', 
                               password = '1234', database = 'webgui')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'

val = [('john','cse','56'),('mike','IT','78'),('tyson','me','80')]

#sql = 'insert into registration (id,name,course,fee) values(%s,%s,%s,%s)'

# #val = [('4','max','software','45000'),
#        ('5','john','nlp','2000'),
#        ('6','mike','boxing','20000'),
#        ('7','tyson','boxer','34000'),
#        ('9','cathy','software','100')]

mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')