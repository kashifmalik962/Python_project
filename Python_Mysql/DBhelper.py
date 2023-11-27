import mysql.connector as mysql
import sys

class DBhelper:
    def __init__(self):
        print('123')
        try:
            self.conn = mysql.connect(host='localhost', user='root', password='',port=3307,database='demo')
            self.mycursor = self.conn.cursor()


        except Exception as e:
            print('Could not Connect to a Database::::',e)
            sys.exit(100)
            
        else:
            print('Connected to Database')

    def register(self, name, email, password):
        try:
            self.mycursor.execute("INSERT INTO `user` (`NAME`, `EMAIL`, `PASSWORD`) VALUES (NULL, '{}', '{}', '{}');".format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        
    def login(self, email, password):

        self.mycursor.execute("""
        Select * from user where email like '{}' and password like '{}'
        """.format(email,password))
        
        data = self.mycursor.fetchall()
        return data
        