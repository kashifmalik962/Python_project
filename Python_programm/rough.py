# lst = [10,20,30,40,50,10,30,20]
# lst2 = sorted(lst, reverse=True)
# print(lst2)


# a = 'one,two,three,four'
# b = a.split(',')
# print(a)
# print(b)


# a = 'this is a ai course'
# b = a.split()
# print(a)
# print(b)



# lst = [10,20,30,40,50,10,30,20]
# print(lst[::-1])


# lst = [10,20,30,40,50,10,30,20]
# lst2 = ['kas','dan','sak']

# for i in range(len(lst)):
#     print(lst[i])


# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)



# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# transposed = []
# for i in range(3):
#     lst = []
#     for j in matrix:
#         lst.append(j[i])
#     transposed.append(lst)
# print(transposed)



# a = (1,(4,5.5,'kash'),['share','string'])
# a[1][0]='kash'
# print(a)
# print(type(a))



# a = ((1,(4,5.5,'kash'),['share','string']) + (1,5,9))
# a = (1,5,3,2,4,6,)
# print(sum(a)/len(a))



# a = {1,2,3,4}
# b = {3,4,5,6}

# print()
# print(a | b)
# print(a.union(b))
# print(a & b)


# a = {2, 3, 5, 6}
# # b = {1, 2, 3, 4}
# # print(a - b)
# # print(a.difference(b))
# b = list(a)
# print(b[2])
# for i in a:
#     print(i)

# d = {1:'kas',2:'mal',3:[1,2,'kas']}
# print(d)
# print(d[3][2])


# d = dict([(1,'kas'),(2,'aah'),(3,'dan')])
# print(d.get('aah'))



# d = {'nae':'kashif','age':20,'eduation':'ba'}
# for i,b in d.items():
#     print(i,b)
# print(d.values())




# d = {'nae':'kashif','age':20,'eduation':'ba'}
# d['nae']='sakib'
# d['town']='islanagar'

# print(d)
# sorted_dict = sorted(d.items())
# print(sorted_dict)
# print(type(sorted_dict))


# a = 'hello world'
# lenght=0
# for i in a:
#     if i=='l':
#         lenght+=1
# print('{} harater found'.format(lenght))




# def nam(local_,global_='that is global'):
#     """
#     this function will return name
#     """

#     local_ = 'that is local var'
#     global_ = 'that is global'

#     print(local_)
#     print(global_)

# print(nam())



# a=20
# b=10
# smaller = a if a < b else b
# print(smaller)



# lst = {1,23,4,7}
# print(lst)
# print(type(lst))
# print(all(lst))

# print(dir(lst))



# print(divmod(18,4))




# lst = [10,20,30,40,50]

# for index,val in enumerate(lst,9):
#     print('index {0} has a value {1}'.format(index,val))
#     if index == 11 | val == 20:
#         break




# number = list(range(-10,10))

# def posi_num(number):

#     if number >=0:
#         return number

# positive_num = list(filter(posi_num , number))
# print(positive_num)




# a = [1,2,3,4,5]

# def pow(arg):
#     return arg**2

# square = list(filter(pow,a))
# print(square)





# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# print(isinstance(a,set))
# print(isinstance(b,list))




# arg = [1,2,3,4,5]

# def pow(arg):
#     return arg**2

# square = list(map(pow,arg))
# print(square)




# def is_even(number):
#   return number**2

# numbers = [1, 2, 3, 4, 5]

# even_numbers = map(is_even, numbers)
# print(type(even_numbers))
# print(list(even_numbers))



# from functools import reduce
# num = [1,2,3,4,5,6,7,4,5,6,1,0]
# def max(x,y):
#     return x if x > y else y

# max = reduce(max,num)
# print(max)    



# from functools import reduce
# import time

# start_time = time.time()
# lst = range(100,1000)
# def multiply(x,y):
#     return x*y

# print(reduce(multiply,lst))

# end_time = time.time()
# print(end_time - start_time)



# import time

# start_time = time.time()
# lst = range(100,1000)
# a = 1
# for i in lst:
#     a*=i
# print(a)
  
# end_time = time.time()
# print(end_time - start_time) 


# dict1 = {'name':'kashif','age':20,'education':'bca','city':'saharanpur','profession':'Data-Scientist'}
# dict2 = {'age': 20, 'city':'saharanpur', 'dob':'1/1/2004', 'region':'India'}




# def goods_deed(**kwargs):
#     '''This Function will provide a message'''
#     if kwargs:
#         print('hello {} , {}'.format(kwargs['name'], kwargs['msg']))

# goods_deed(name='kashif', msg='good morning')




# def greet(*names):

#     print(names)
#     for i in names:
#         print('hello {} , good morning'.format(i))

# greet('kashif','danish','aahad','aamir','sumoon')



# def pow(num):
#     return num**2

# num = (1,2,3,4,5)

# squ_num = list(map(pow,num))
# print(squ_num)






# def facto(num):

#     return 1 if num == 1 else (num *facto(num-1))

# num = 5
# print("factorial of {0} is {1}".format(num, facto(num)))




# def greet(**kwargs):
#     '''this function will return greet to employee'''

#     if kwargs:
#         print('hello {} good {}'.format(kwargs['name'],kwargs['time']))

# greet(name='kashif',time='morning')




# def greet(*names):
#     '''this function will return greet to employee'''

#     print(names)
#     if names:
#         for index,name in enumerate(names):
#             if index >= 3:
#                 print('hello {} good evening'.format(name))
#             else:
#                 print('hello {} good morning'.format(name))

# greet('kashif','aahad','salman','afjal','aamir','sakib')
# print(greet.__doc__)




# def factorial(num):

#     if (num == 0 or num == 1):
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(4))





# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))    
# print()
# for num in range(7):
#     print(fibonacci(num))



# double = lambda x: x**2
# print(double(20))


# from functools import reduce

# lst = [1,2,3,4,5]
# even_lst = reduce(lambda x,y: x*y,lst)
# print(even_lst)



# import datetime

# a = datetime.datetime.now()
# print(a)


# def fab(num):
#     '''this func will return fibnachhi series'''

#     if num<=1:
#         return num
    
#     else: 
#         return fab(num-1) + fab(num-2)

# for i in range(10):
#     print(fab(i))





# def fib(n):
#     '''this func will return fib series'''

#     if (n==0 or n==1):
#         return n
    
#     else:
#         return fib(n-1) + fib(n-2)
    

# for i in range(10):
#     print(fib(i))



# import sys

# lst = [0,'b',2]
# for i in lst:

#     try:
#         print('the entry is a',i)
#         if 1/i:
#             print('this {} entry perfectly division by 1'.format(i))

#     except(ValueError):
#         print('this is a value error')
#     except(TypeError):
#         print('this is a type error')
#     except(ZeroDivisionError):
#         print('this is a Zerodivision error')
#     except:
#         print('some other error')
#     finally:
#         print('Its a good programming')




# def seq():
#     for i in range(1,10):
#         if i==2:
#             print('hey')

# seq()




# import pdb

# def seq(n):
#     for i in range(n):
#         pdb.set_trace()
#         print(i)

# seq(5)




# import pdb

# bike1 = 'hero'
# bike1_price = 80000

# bike2 = 'honda'
# bike2_price = 90000

# name = input('enter the name :')
# print(f'hello {name}')

# pdb.set_trace()

# choose = input('enter the bike :')
# if choose == 'hero':
#     print(f'the price of {bike1} bike {bike1_price+2000}')

# elif choose == 'honda':
#         print(f'the price of {bike2+2000} bike {bike2_price}')

# else:
#       print('the bike will not exist the agency')



# i = 0
# while True:
#   i+=1
#   if i == -100:
#     break
#   print("Hello, world!")

# import numpy

# arr = numpy.sort(numpy.random.randint(1,1000,800))
# # print(arr)
# counter = 0

# for index,i in enumerate(arr):
#     counter+=1
#     if i == 498:
#         print(index,counter)




# arr = numpy.sort(numpy.random.randint(1,1000,700))

# n = 62
# low = 0
# high = len(arr) - 1
# counter = 0
# # print(low,high,arr,n)

# while low <= high:
#     counter+=1
#     mid = (low+high)//2
#     if arr[mid] == n:
#         print(mid)
#         break
    
#     elif arr[mid] > n:
#         high = mid - 1
    
#     else:
#         low = mid + 1
    
# if low > high:
#   print('number not available in list')





# dic = {"employe":{"kashif":{'Id':1,'salary':20000,'designation':'DS'},
#                     "Danish":{"Id":2,"salary":22000,"designation":"FSD"},
#                     "aahad":{"Id":3,"salary":180000,"designation":"DE"}}}
# print(dic['employe']['Danish']['salary'])

# print(dic.keys())



# my = {'Id':1,'salary':20000,'designation':'DS'}
# my.update({"salary": 50000})
# print(my.popitem())
# print(my)


# com_ele = []
# cnt = 0
# cnt2 = 0
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [64,11,12,14,5,1,6,48,65]
# for i in a:
#     cnt+=1
#     for j in b:
#         cnt2+=1
#         if i == j:                                         # n^2
#             com_ele.append(i)
#         else:
#             pass

# print(com_ele)
# print(cnt+cnt2)




# list1 = [1,2,3,4,5,6,7,8,9,10,11]
# for i in list1:
#     print(id(i))


import numpy as np

# ar = np.array([1,2,3,4,5,6,7,8,9,10])
# print(id(ar))
# print(ar)
# # for i in ar:
# #     print(id(i))
 
# ar = [1,2,3,4,5,6]
# print(ar)
# import sys

# integer_size = sys.getsizeof(ar[1])

# print(integer_size)

# ar = np.array([[1,2,3],[4,'5',6],[7,8,9]])
# ar[0][0]=10
# print(ar)



# l = [2200,2350,2600,2130,2190]
# # In Feb, how many dollars you spent extra compare to January
# print(abs(l[0]-l[1]))
# # Find out your total expense in first quarter (first three months) of the year
# print(l[0]+l[1]+l[2])
# # Find out if you spent exactly 2000 dollars in any month
# for index,i in enumerate(l):
#     if i == 2000:
#         print(l[index])
# else:
#     print("We can't' spent exactly 2000 dollars in any month")

# # June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

# l.insert(5,1980)
# print(l)

# l[3] = 2130-200
# print(l)



# # Length of the list
# heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))

# # Add 'black panther' at the end of this list
# heros.append('black panther')
# print(heros)

# # You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'

# heros.pop()
# print(heros)

# heros.insert(3,'Black panther')
# print(heros)

# # Now you don't like thor and hulk because they get angry easily :)
# # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# # Do that with one line of code

# heros[1:3] = ['Doctor strange']
# print(heros)

# # Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# heros.sort()
# print(heros)


# def odd(n):
#     for i in range(1,n):
#         # print(i)
#         if i%2!=0:
#             print(i)

# n = int(input('Enter a maximum number :'))

# odd(n)