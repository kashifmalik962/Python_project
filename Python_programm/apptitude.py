# print(print(print('Kashif')))
# print(True**False/True)
# x = 5
# y = 3
# if x!=y:
#     y = --y
#     print(x-y)

# print(int(6==6.0)*3+4%5)  

# print(6+5-4*3/2%1)

# a = 0b0110
# print(a)

# a = 'kashif'
# print(*a)


# x = 2,
# y = 3,4
# z = x+y
# print(z)

# a = 10,20
# b = 30,40
# print(a+b)
# print(type(a+b))


# n = int(input('eentrgbgg : '))
# s = ''
# for i in range(1,n+1):
#     s = s + str(i)
# print(type(s))    


# n = int(input())
# if (n[0] == '+' or n[0]=='-' or n[0]=='.') and (n[1]!='+' and n[1]!='-'):
#     if '.' in n:
#         result = n.split(".")
#         print(result[1]=='')




# print(len([[[10,20],[30,40]]]))


# x = [0,1,2,3,4]
# x.append(x[:])
# print(len(x))
# print(x)


                            # EXTEND FUNCTION RETURN NONE

# x = [1,2]
# y = [3,4]
# x.extend(y)
# print(x)




# x = [1,2]
# y = [3,4]
# z = x.extend(y)
# print(z)


# x,*y = 10,20,30,40
# print(x,y)
# print(type(x),type(y))



                                #  FACTORAIL


# def user_input(n):
#     a = 1
#     b = 0
#     for i in range(1,n+1):
#         a = a*i
#         b = b+1
#         print(b)
#         if n <= a:
#             break
# user_input(120)


                                    # PRIME NUMBER

# def prime(n):


#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False

#     return True       

# print(prime(25))




                            # FABNICCO SERIES


# def fab(n):
#     a,b = 0,1
#     for i in range(n):
#         print(a)
#         c = a+b
#         a = b
#         b = c
# fab(10)


                          
                            # PALENDROME



# a = 'malayalam'
# n = len(a)
# b = n/2
# c = 0
# Palendrome = True

# for i in range(int(b)):
#     c = c+1
#     if a[i]==a[n-1-i]:
#         pass
#     else:
#         Palendrome = False
# print(Palendrome,c)



                                    # GCD NUMBER



# def lcm(a,b):
#     GCD = True
#     while True:
#         print(a,b)
#         if a%b==0:
#             return GCD
              
#         else:
#             b = int(a%b)
#         print(a,b)
# print(lcm(10,3))




                                # SUM OF NATURAL NUMBER


# def natural(n):
#     a = 0
#     if n==0:
#         return 0
#     for i in range(1,n+1):
#         a = a+i
#     print(a)

# natural(5)



                                # REVERSE A NUMBER


# def reverse(n):
#     if n == 1 or n == 0:
#         return 'greater then 2'
#     else:
#         for i in range(n,0,-1):
#             print(i)
# reverse(200)






                            # FIND THE LARGEST NUMBER IN LIST

# b = [0]
# a = [10,5,9,8,4,2,3,7,5,7,5,50,40,33,22,44]
# lar = a[0]
# for i in range(1,len(a)):
#     if a[i] > lar:
#         lar = a[i]
# print(lar)
    
    

                            # REVERSE A STRING


# def rev_string(n):
#     a = []
#     for i in range(len(n)-1,-1,-1):
#         a.append(n[i])
#         print(n[i])
#     print(a)

# rev_string('starkashif')
    



                            # CHECK IF NUMBER IS PRIME


# def check_prime(n):
#     for i in range(2,n+1):
#         if n % i==0:
#             return False
#         else:
#             return True
#     else:
#         return 'Invalid'
    
# print(check_prime(19))







# print("Hello, " + input("What is your name? "))





                        # FIND LARGEST ELEMENT IN A LIST


# def lar_ele_list(n):
#     a = 0
#     for i in n:
#         if a <= i:
#             a = i

#     print(a)

# lar_ele_list([1,2,3,40,5,60,7])




                        # FIND SMALLEST ELEMENT IN A LIST





# def lar_ele_list(list):
#     b = list[0]
#     for i in range(1,len(list)):
#         if b > list[i]:
#             b = list[i]
#     print(b)

# lar_ele_list([5,2,3,40,5,60,7])




                        # FIND THE AVERAGE OF NUMBER A LIST



# def average_list(n):
#     a = []
#     b = 0
#     c = 0
#     for i in n:
#         b +=1
#         a.append(i)
#         c = a/b
#     print(a)


# average_list([5,2,3,40,5,60,7])

   



                                 # SIMPLE INTEREST   (A = P*R*T/100)



# n = int(input("Enter the initial amount :"))
# if n > 0:
#     print(n*5*2/100)
# else:
#     print("Invalid detail")





                                # COMPUOND INTEREST   (A = P*(1+R/N)^(N*T))


# n = int(input("Enter the initial amount :"))

# if isinstance(n, int):
#     print(n * (1 + 20/100) ** 1)
# else:
#     print("Invalid Detail")




                                # ARMSTRONG NUMBER



def armstrong(num):

    strnum = str(num)
    print(strnum[0],strnum[1])
    a = (int(strnum[0]))*(int(strnum[1])),(int(strnum[2]))
    print(a)
armstrong(121)
