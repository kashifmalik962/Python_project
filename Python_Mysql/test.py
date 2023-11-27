import mysql.connector

db = mysql.connector.connect(host='localhost',user="root'@'localhost",password='',database='python')
print(db)

if(db):
    print('s')

else:
    print('N')