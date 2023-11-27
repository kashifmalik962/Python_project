import mysql.connector

class DBhelper:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', password='78654321', database='demo')
        print(self.conn.connection_id)