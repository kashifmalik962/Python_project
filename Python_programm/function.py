def add_fun():
    a = 10
    b = 20
    c = a+b
    print(c)

add_fun()



a = 10




# def add_name():
#     a = 'KASHIF'
#     print('Welcome to',a)

# add_name()



# def add_name(b):
#     a=10
#     c = a+b
#     print(c)

# add_name(20.5)




# def divide_name(b):
#     a=10
#     c = a/b
#     print(c)

# divide_name(2)




# def add():
#     a = 10
#     b = 20
#     c = a+b
#     d = c-b

#     return (d,c,a,b,50)

# sub,sum,a,b,value = add()
# print(sum,sum,a,b,value)



# def sum(b):
#     a=10
#     c=a/b
#     d = c-b
#     return a,b,c,d

# print(sum(20))




# def outer_func():
#     def inner_func():
#         print('inner')
#     print('outer')
#     inner_func()
# outer_func()



# def out():
#     def inner():
#         return 'kashif'
#     result = inner()+" " + 'malik' +' islamnagar'
#     return result
# print(out())



# def inner2():
#     return 'malik'

# def inner3():
#     return 'kashif'

# def out1():
#     def inner1():       
#         return 'islamnagar'
#     result = inner3()+"  "+inner2()+"  "+inner1()
#     return result
# print(out1())


# def func1(st):
#     return 'kashif'+st()

# def func2():
#     return 'malik'

# print(func1(func2))


# def func(name, age=27):
#     print(name,age)

# func(age=19,name='kashif')



# def sum(*add):
#     print(add[0]+add[1]+add[2]+add[3])

# sum(10,20,30,40)


# def out():
#     def inner():
#         print('inner')
#     print('out')
#     inner()
# out()



                                            # LAMBDA

# ka = lambda x : print(x)
# ka(10)


# lm = lambda x,y : (x+y,y-x)
# a,s = lm(10,20)
# print(a)
# print(s)


# lm = lambda x,y,z: (x+y*2, y-x*2, y/x*2)
# a,s,z = lm(10,20,10)
# print(a)
# print(s) 
# print(z)



# lm = lambda x=10,y=20,z=30: (x+y*2, y-x*2, y/x*2)
# a,s,z = lm()
# print(a)
# print(s) 
# print(z)



# lm = lambda x,y : print((x+y,x-y))
# lm(10,20)



# add = lambda x=10: (lambda y :x+y)
# a = add()
# print(a(20))




# def func():
#     y = 20
#     return lambda x: x+y

# a = func()
# print(a(10))



# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def div(x,y):
#     return x/y

# def mul(x,y):
#     return x*y

# print('1. ADD')
# print('2. SUBTRACT')
# print('3. DEVIDE')
# print('4. MULTIPLY')

# while True:
#     choice = input('Enter Number(1,2,3,4) :')

#     if choice in ('1', '2', '3', '4'):
#         try:
#              num1 = float(input('Enter First Number :'))
#              num2 = float(input('Enter Second Number :'))
#         except ValueError:
#             print('Invalid Number Try Again :')
#             continue
#         if choice == '1':
#             print(num1,'+', num2,'=', add(num1,num2))
        
#         elif choice == '2':
#             print(num1,'-',num2,'=',sub(num1,num2))
        
#         elif choice == '3':
#             print(num1,'/', num2,'=', div(num1,num2))

#         elif choice == '4':
#             print(num1,'*', num2,'=',mul(num1,num2))

#         next_calculation = input('next_calculation yes/no :')
#         if next_calculation == 'no':
#             break
        
#         else:
#             print('invalid input')




# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def div(x,y):
#     return x/y

# def mul(x,y):
#     return x*y

# while True:
#     choice = input('Enter Number 1,2,3,4 :')
#     if choice in ('1','2','3','4'):
#         try:
#             num1 = float(input('Enter First No :'))
#             num2 = float(input('Enter Second No :'))
#         except ValueError:
#             print('invalid Input')
#             continue

#         if choice == '1':
#             print(num1,'+',num2,'+', add(num1,num2))
        
        
#         if choice == '2':
#             print(num1,'+',num2,'+', sub(num1,num2))

        
#         if choice == '3':
#             print(num1,'+',num2,'+', div(num1,num2))

        
#         if choice == '4':
#             print(num1,'+',num2,'+', mul(num1,num2))

#         next_cal = input('next_calculation (yes/no) :')
#         if next_cal == 'no':
#             break

#         else:
#             print('Invali')



