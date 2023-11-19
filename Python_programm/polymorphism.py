                                    #  DUCK TYPING

# class Duck:
#     def walk(self):
#         print('Thapak Thapak Thapak Thapak')

# class Horse:
#     def walk(self):
#         print('Tabdak Tabdak Tabdak tabdak')

# d = Duck()
# h = Horse()

# def myfunct(obj):
#     obj.walk()

# myfunct(h)




                                    #  STRONG TYPING



# class Duck:
#     def walk(self):
#         print('Thapak Thapak Thapak Thapak')

# class Horse:
#     def walk(self):
#         print('Tabdak Tabdak Tabdak tabdak')


# class Cat:
#     def talk(self):
#         print('Mew Mew Mew Mew')

# d = Duck()
# h = Horse()
# c = Cat()

# def myfunct(obj):
#     if hasattr(obj,'walk'):
#         obj.walk()
#     if hasattr(obj,'talk'):
#         obj.talk()
# myfunct(c)



                                      # OPERATOR OVERLOADING
# print(str.__add__('kas','hif'))


# class A:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self,other):
#         sum = self.x + other.x
#         return sum

# class B:
#     def __init__(self, x):
#         self.x = x

# a = A(100)
# b = B(200)
# print(a+b)


    # def ad(x,o):
    #     self = x
    #     other = o
    #     return int.__add__(x,o)

    # print(ad(10,20))



                                        # METHOD OVERLOADING


# class Myclass:
#     def sum(self,a):
#         print('2nd method',a)
    
#     def sum(self):
#         print('1st method')

# ob = Myclass()
# ob.sum()
# ob.sum(10)




# class Myclass:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#             return s
    
#         elif a!=None and b!=None:
#             t = a*b
#             return t
        
#         elif a!=None and c!=None:
#             u = a-c
#             return u
        
#         else:
#             print('Provide at least 2 number')

# ob = Myclass()
# print(ob.sum(10))




# class Add:
#     def result(self,a,b,c):
#         s = a+b+c
#         print(s)

# class Mul(Add):
#     def result(self, a, b, c):
#         super().result(10,20,30)
#         m = a*b*c
#         print(m)

# ob = Mul()
# ob.result(10,20,30)







