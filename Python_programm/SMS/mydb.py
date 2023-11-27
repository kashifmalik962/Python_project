import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        print('123')
        print(dir(mysql.connector))
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='password', database='demo')
            print('456')
            self.mycursor = self.conn.cursor()
        
        except Exception as e:
            print('Could not Connect to a Database::::',e)
            sys.exit(100)
            
        else:
            print('Connected to Database')


db = DBhelper()            