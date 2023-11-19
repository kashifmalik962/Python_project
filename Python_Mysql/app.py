import sys
from DBhelper import DBhelper

class Flipkart:

    def __init__(self):
        # connect to a database
        self.db = DBhelper()
        self.menu() 

    
    def menu(self):
        
        user_input = input("""
        1. Enter 1 to Register
        2. Enter 2 to Login
        3. Anything else to leave
        """)

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else: 
            sys.exit(100)
    
    def register(self):
        name = input('Enter the name :')
        email = input('Enter the email :')
        password = input('Enter the password :')
        
        response = self.db.register(name, email, password)

        if response:
            print('Registration successful')
        else:
            print('Registration failed')
    
        self.menu()

    
    def login(self):
        email = input('Enter the email :')
        password = input('Enter the password :')
        data = self.db.login(email, password)

        if len(data) == 0:
            print('Incorrect email/password')
            self.login()
        else:
            print('Hello',data[0][1])
        
obj = Flipkart()