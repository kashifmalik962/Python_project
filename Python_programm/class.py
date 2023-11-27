# class Myclass:
#     def show(self):
#         return 'I am Kashif'

# k = Myclass()
# print(k.show())



# class Mobile:
#     def __init__(self):
#         self.model = 'Realme X'

#     def show_model(self):
#         Price = 10000
#         print('Model :',self.model,"|", "Price :", Price)

# x = Mobile()
# x.show_model()




# class Mobile:
#     def __init__(self,m):
#         self.model = m
    
#     def show(self,p,c):
#         Price = p
#         Color = c
#         print("Model :",self.model,"|", "Price :", Price,"|", "Color :", c)

# realme = Mobile('Realme X')
# realme.show(10000, "Red")
# print(id(realme))
# print()

# redmi = Mobile('Redmi')
# redmi.show(20000, "Blue")
# print(id(redmi))





# class Mobile:
#     def __init__(self,m):
#         self.model = m

#     def show(self,p,c,s):
#         Price = p
#         Color = c
#         Size = s
#         print("Model :",self.model, "|", "Price :", Price,"|", "Color :", Color, "|", "Size :", Size)

# ob = Mobile("Apple :")
# ob.show(100000,"Gold", "10*10")




# class Mobile:
#     def __init__(self,m):
#         self.model = m

#     def show(self,p,c,m):
#         Price = p
#         Color = c
#         Model_No = m
#         print("Model :",self.model,"|","Price :" ,p, "|", "Color :", c, "|", "Model No :", m)

# ob = Mobile("IPhone 12 Pro")
# ob.show(100000, "Gold", 124578963)




# class Mobile:
#     fp = 'yes'
#     def __init__(self):
#         self.model = 'Realme X'
#     def show(self):
#        print(self.model)
#     @classmethod
#     def is_fp(cls):
#        print(cls.fp)
# ob = Mobile()
# print(ob.fp)
# ob.fp = 'No'
# print(ob.is_fp())
# print(ob.fp)




# class Mobile:
#     fp = 'no'

# Mobile.fp = 'not work'
# print(Mobile.fp)
# realme = Mobile()
# realme.fp = 'yes'
# print(realme.fp)




# class Mobile:
#     def __init__(self):
#         self.model = 'Realme X'
#     def show(self,c,p,r):
#         self.model = 'Redmi  Pro'
#         color = c
#         price = p
#         rating = r
#         print("Model :",self.model,"|", "Color :", color,"|","Price :", price,"|", "Rating :", rating)
        

# ob = Mobile()
# ob.show('red',100000,5.1)




# class Mod:
#     @classmethod
#     def show(cls):
#        return 'kashif'

# ob = Mod()
# print(ob.show())



# class Mob:
#     fp = 'kashif'

# ob = Mob()
# print(ob.fp)





# class Mobile:
#     ab = 'Realme X'
#     @ classmethod   
#     def show(cls,r):
#         cls.ram = r
#         print(cls.ab, r)

# ob = Mobile()
# ob.show('4GB')





# class Mobile:
#     @staticmethod
#     def show(m,c,r):
#         mobile = m
#         color = c
#         ram = r
#         print(m,c,r)

# ob = Mobile()
# ob.show('Realme','red','4GB')




# class Mobile:
#     def __init__(self):
#         self.model = 'Realme X'
#         self.ram = '4GB'
#         self.rom = '128 GB'
#         print(self.model,self.ram,self.rom)

# ob = Mobile()
# ob




# class Student:
#     def __init__(self,n,r,c):
#         self.name = n
#         self.roll = r
#         self.step = c
#     def show(self):
#         print(self.name, self.roll, self.step)


# class User:
#     @staticmethod
#     def desp(n):
#         print('User_Name :',n.name)
#         print('User_Roll :',n.roll)
#         print('User_Clas :',n.step)
#         n.show()
# ob = Student('Kashif',101,'6th')
# User.desp(ob)









# class Sir:
#     def __init__(self,m,r,c,p):
#         self.mobile = m
#         self.ram = r
#         self.color = c
#         self.price = p

#     def student(self):
#         print("Sir :",self.mobile,self.ram,self.color, self.price)


# class User:
#     @staticmethod
#     def show(n):
#         print(n.mobile)
#         print(n.ram)
#         print(n.color)
#         print(n.price)



# ob = Sir('Realme','4GB','Gold',10000)
# User.show(ob)






# class Army:
#     def __init__(self):
#         self.name = 'Javed'   
#         self.gn = self.Gun()
#     def show_name(self):
#         print(self.name)
    
#     class Gun:
#         def __init__(self):
#             self.gun = 'AK47'
#             self.capacity = '75 Round'
#             self.length = '35 inch'
        
#         def show_feature(self):
#             print(self.gun, self.capacity, self.length)

# a = Army()
# print(a.name)
# a.gn.show_feature()



# class Mobile:
#     def __init__(self,m):
#         self.model = m

#     def show(self,p,c,r):
#         self.price = p
#         self.color = c
#         self.Ram = r
#         print(self.model,self.price,self.color,self.Ram)

# ob = Mobile('Realme X')
# ob.show(10000,'Gold','4GB')


# class Mobile:
#     ab = 'Redmi X'

#     @classmethod
#     def show(cls,m):
#         cls.model = m
#         print(cls.ab,cls.model)
    
# ob = Mobile()
# ob.show('Apple')



# class Teacher:
#     def __init__(self):
#         self.name = 'Kashif'
#         self.adress = 'Islamnagar'
#         self.subject = 'ML'
#         self.mobile = '9149076448'
        
#     def tech_show(self):
#         print(self.name,self.adress,self.subject,self.mobile)

# class Student:
#     @staticmethod
#     def show(s):
#         s.tech_show()

# ob = Teacher()
# print(Student.show(ob))



# class Sir:
#     def __init__(self,m,r,c,p):
#         self.mobile = m
#         self.ram = r
#         self.color = c
#         self.price = p

#     def student(self):
#         print("Sir :",self.mobile,self.ram,self.color, self.price)


# class User:
#     @staticmethod
#     def show(n):
#         print(n.mobile)
#         print(n.ram)
#         print(n.color)
#         print(n.price)



# ob = Sir('Realme','4GB','Gold',10000)
# User.show(ob)





# class Teacher:
#     def __init__(self):
#         self.name = 'danish'
#         self.adress = 'Islamnagar'
#         self.subject = 'ML'
#         self.mobile = '9149076448'
#         self.st = self.Student()
        
#     def tech_show(self):
#         print(self.name,self.adress,self.subject,self.mobile)

#     class Student:
#         def __init__(self):
#             self.name = 'sakib'
#             self.result = 'pass'

#         def stu_show(self):
#             print(self.name,self.result)

# a = Teacher()
# a.st.stu_show()




# class Teacher:
#     def __init__(self):
#         self.name = 'Afjal'
#         self.age = 30
#         self.st = self.Student()
#     def student(self):
#         print(self.name, self.age)

#     class Student:
#         def __init__(self):
#             self.name = 'Kashif, Danish, Aahad'
#             self.Age = "19,19,19"
#         def show(self):
#             print('name :',self.name, 'Age :',self.Age)

# te = Teacher()
# print(te.st.name)


# from datetime import date
# d1 = date(2022,11,15)
# d2 = date(2019,8,22)
# print(d1!=d2) 



# from datetime import datetime
# d = datetime.today()
# print(d)


# import time
# for i in range(20):
#     if i ==10:
#         time.sleep(2)
#     print(i)



from datetime import date

td = date.today()
rd = date(2004,1,1)

print(td)
print(rd)
print(td-rd)

