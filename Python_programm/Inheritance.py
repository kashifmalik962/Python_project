# class Father:
#     ab = 'This is a My first Parent Class'
#     def __init__(self):
#         self.name = 'Anas'
#         self.gender = 'Male'
    
#     def show(self):
#         print('Parent Class Instance Method :',self.name, self.gender)
    
#     @classmethod
#     def clas_method(cls):
#         print(cls.ab)
    
#     @staticmethod
#     def stat_method():
#         a = 10
#         print('Parent Class Static Method',a)

# class Son(Father):
#     def show_son(self):
#         print('Child Class Instance Method :')

# a = Son()
# a.show_son()
# a.show()
# a.clas_method()
# a.stat_method()




# class Parent:
#     pr = 'This is Parent Class'
#     def __init__(self):
#         self.name = 'Anas'
#         self.gender = 'Male'
    
#     def show(self):
#         print('Name :', self.name)
#         print('Gender :', self.gender)

#     @classmethod
#     def clsprmethod(cls):
#         print(cls.pr)

# class Son(Parent):
#     sn = 'This is Child Class'
#     def __init__(self):
#         self.name = 'Danish'
#         self.gender = 'Male'

#     def disp(self):
#         print('Name :', self.name)
#         print('Gender :', self.gender)

#     @classmethod
#     def clssonmethod(cls):
#         print(cls.sn)

# s = Son()
# s.clssonmethod()


# class Parent:
#     def __init__(self):
#         self.name = 'ajjal'
#         print('this is parent class const')

#     def show(self):
#         print(self.name)

# class Son(Parent):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Afjal'
#         print('This is Child class const')
#     def disp(self):
#         print('this is son class')

# s = Son()
# print(s.name)







                                            # MULTI-LEVEL INHERITANCE



# class Parent:
#     def __init__(self):
#         self.money = 100000
#         self.vehical = "Scooter"
#         print('Money :', self.money)
#         print('Vehical :', self.vehical)
    
#     def parshoww(self):
#         print("Parent class Instance Method")

# class Son(Parent):
#     def __init__(self):
#         super().__init__()
#         self.money = 500000
#         self.vehical = "Bike"
#         print("Money :", self.money)
#         print("Vehical :", self.vehical)


#     def sonshoww(self):
#         print("Son class Instance Method")

# class Grandson(Son):
#     def __init__(self):
#         super().__init__()
#         self.money = 1000000
#         self.vehical = "Car"
#         print("Money :", self.money)
#         print("Vehical :", self.vehical)


#     def grandshoww(self):
#         print("Grandson class Instance Method")


# ob = Grandson()

# print()
# ob.parshoww()
# ob.sonshoww()
# ob.grandshoww()




# class Father:
#     def __init__(self):
#         print('Father class Constructer')
#     def showF(self):
#         print('Father class Mehthod')

# class Son(Father):
#     def __init__(self):
#         print('Son class Constructer')
#     def showS(self):
#         print('Son class Mehthod')

# class Daughter(Father):
#     def __init__(self):
#         super().__init__()
#         print('Daughter class Constructer')
#     def showD(self):
#         print('Daughter class Mehthod')

# # f = Father()
# # s = Son()
# d = Daughter()

# print()

# d.showD()




class Father:
    def __init__(self):
        print('Father class Constructer')
    def showF(self):
        print('Father class Method')



class Mother:
    def __init__(self):
        print('Mother class Constructer')
    def showM(self):
        print('Mother class Method')



class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print('Son class Constructer')
    def showS(self):
        print('Son class Method')


s = Son()
s.showM()