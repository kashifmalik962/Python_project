#                                   LIST


# a = [10,20,-50,'kashif']
# print(a, id(a))
# a[1]=30
# print(a, id(a))


# a = [10,20,-50,'kashif']
# print(len(a))
# for i in a:
#     if i==-50:
#         continue
#     print(i)

# a = [10,20,-50,2.5,'kashif',]
# n = len(a)
# for i in range(n):
#     print(i,'=',a[i])

# a = [10,20,-50,2.5,'kashif']
# n = len(a)
# i = 0
# while i<n:
#     print(a[i])
#     i+=1

# a = [10,20,-50,2.5,'kashif']
# a.append(100)
# print(a)


# a = [10,20,-50,2.5,'kashif',]
# a.append(100)
# n = len(a)
# for i in range(n):
#     print(i,'=',a[i])


# a = []
# print(a)
# n = int(input('enter the element :'))
# for i in range(n):
#     a.append(int(input('enter element :')))
# print(a)


# a = [10,20,-50,2.5,'kashif']
# a.insert(2,33)
# a.pop()
# a.remove(33)
# a.reverse()
# for i in a:
#     print(i)


# a = [10,20,-50,2.5,]
# b = [10,10,60,70,]
# a.extend(b)
# print(a.sort(),a)


# a = [10,20,-50,2.5,]
# b = [10,10,60,70,]
# a.extend(b)
# a.clear()
# print(a)


# a = [10,20,-50,2.5,]
# b = [10,10,60,70,]
# a.extend(b)
# c = a[0:5]
# print(c)


# a = [10,20,-50,2.5,]
# b = [10,10,60,70]
# c = [80,90,100]
# lt = a+b+c
# print(lt)


# a = [10,20,-50,2.5]*2
# b = [10,10,60,70]
# print(a+b)


# a = [10,20,-50,2.5]
# b = a*3
# print(b)


# a = [10,20,-50,2.5]
# a[1]=500
# b = a
# print(b)


# b = [70,80,90]
# a = [10,20,30,[40,50,60],b]
# print(a[4][0])



# a = list(range(1,100))
# print(a)
# print(type(a))


# a = list(range(1,100))
# print(a)



#                                               TUPLE  

# a = (10,)
# print(type(a))


# a = 10,20,30,40,40,'kashif'
# print(type(a))

# a = tuple()
# print(type(a))


# a = (10,20,30,40,40,'kashif')
# print(a[2])


# a = (10,20,30,40,40,'kashif')
# n = len(a)
# for i in range(n):
#     print(i,'=',a[i])


# a = (10,20,30,40,40,'kashif')
# n = len(a)
# i = 0
# while i<n:
#     print(i,'=',a[i])
#     i+=1


# a = (10,20,30,40,40,'kashif')
# b = (50,60,70)
# c = a+b
# print(c)
# print(id(a))
# print(id(b))
# print(id(c))


# a = (10,20,30,40,40,'kashif')
# b = a[0:3]
# print(b)


# a = (10,20,30,40,40,'kashif')
# print(a.index(20))
# print(a)

# a = (10,20,30,40,40,'kashif')
# b = a[0:3]
# print(b)


# a = (10,20,30,40,40,'kashif')
# b = a[0:3]
# c = a[5:]
# d = (50,)

# e = b+d+c
# print(e)



# a = (10,20,30,40,40,'kashif')*4
# print(a)
# b = a[:4]
# c = a[5:]
# print(b+c)


# a = []
# n = int(input('enter number of element :'))

# for i in range(n):
#     a.append(int(input('enter element :')))
# a = tuple(a)
# print(a)
# print(type(a))



# a = (10,20,30,40,40,'kashif')
# a = (20,30,40)
# a = ('kashif',10,'malik')
# b = a
# print(a)


# a = (10,20,30,40,40,'kashif')
# b = a[0:6]
# print(b)

# a = (10,20,30,40,(40,'kashif'))
# b = ('malik',50,60,70)
# c = a+b
# print(c[4][1])


# a = (10,20,30,40,40,'kashif')
# n = len(a)
# for i in range(n):
#     if a[i]==40:
#         continue
#     print(i,'=',a[i])
    

# a = [10,20,30,40,(40,'kashif')]
# a.append((60,70))
# n = len(a)
# for i in range(n):
#     print(i,'=',a[i])



# a = [10,20,30,40,(40,'kashif')]
# b = tuple(a)
# print(type(b))



# a = [10,20,30,40,(40,'kashif')]
# a[0]=5
# print(a)


# a = (10,20,30,40,[40,'kashif'])
# a[4][0]=50
# print(a)
# print(type(a))



# a = (20,10,30,50,40,'kashif')
# print(a)





#                                         SET

# a = {20,10,30,50,40,40,'kashif'}
# print(type(a))



# a = {20,10,30,50,40,'kashif'}
# b = {60,70,80}
# print(a+b)


# a = {20,10,30,50,40,'kashif'}
# a.update([100,200,300])
# print(a)
# print(type(a))


# a = {20,10,30,50,40,'kashif'} 
# a.discard(50)
# print(a)


# a = {10,20,30,'kashif'}
# print(type(a))
# print(a)






#                                       DICTIONARY



# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# a[101]='javed'
# a[106]='kashif'
# a[105]='afjal'
# print(a)



# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# del a[101]
# print(a)



# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# print(a)
# del a 
# print(a)


# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# print(101 in a)



# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# print(a)
# a.clear()
# print(a)


# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# a[105]='javed'
# del a[104]
# print(a)

# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# print(101 in a)

# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# print(a)
# a.clear()
# print(a)


# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# b = a.copy()
# print(a)



# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# print(a.get(101))


# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# b = a.items()
# c = list(b)
# print(c[0][0])



# a = {101:'kashif',102:'salman',103:'aahad',104:'aamir'}
# b = a.items()
# c = list(b)

# for r in c:
#     for d in r:
#         print(d)


# a = [2, 5, 4]
# a.sort()
# print(a)



# a = (1,2,1,3,4,5,6)
# i = 0
# n = len(a)
# while i<n:
#     print(i)
#     i+=1



# a = (1,2,1,3,4,5,6)
# b = (7,8,9,10)
# c = a+b
# print(c)



# a = (1,2,1,3,4,5,6)
# b = a[:]
# print(b)


# a = (1,2,1,3,4,5,6)
# del a
# print(a)


# a = (1,2,1,3,4 ,5,6,'kashif',7,9,8)*2
# print(a)



# a = []
# n = int(input('enter the element :'))

# for i in range(n):
#     a.append(int(input('enter element :')))

# for element in a:
#     print(a.append(element))



# a = 'aannaa'
# n = len(a)
# b = n/2
# c = 0
# polydrome = True
# for i in range(int(b)):
#     c = c+1
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         polydrome = False
# print(polydrome,c)


# a = 'aanaa'
# n = len(a)
# polydrome = True
# for i in range(n):
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         print(polydrome)


# a = 121
# a = str(a)
# n = len(a)
# b = n/2
# c = 0
# polydrome = True
# for i in range(int(b)):
#     c = c+1
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         polydrome = False
# print(polydrome,c)




# a = 121
# a = str(a)
# n = len(a)
# b = n/2
# polydrome = True
# for i in range(int(b)):
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         polydrome = False
# print(polydrome)



# n = 121
# b = n
# a = 0
# while b>0:
#     rem = b%10
#     a = a*10+rem
#     b = b//10
#     if a==n:
#         print('yes')
#     else:
#         print('no')







# a = 121
# b = a
# c = 0
# while b>0:
#     rem = b%10
#     c = c*10+rem
#     b = b//10
#     if a==c:
#         print('yes')
#     else:
#         print('no')    




# a = 121
# n = len(a)
# b = n//2
# c = 0
# palendrome = True
# for i in range(b):
#     c = i+1
#     print(c)
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         palendrome = False
#         break
# print(palendrome)

# filter(lambda x,y: x==y)



# a = 'malayalam'
# n = len(a)
# palendrome = True
# for i in range(int(n)):
#     if a[i]==a[n-1-i]:
#         pass
#     else:
#         palendrome = False

# print(palendrome)
    


# a = 'aannaa'
# n = len(a)
# polydrome = True
# for i in range(int(n)):
#     if a[i]==a[n-1-i]:
#         pass
#     else:
#         polydrome = False
# print(polydrome)





# a = 'aanaa'
# n = len(a)
# polydrome = True
# for i in range(n):
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         print(polydrome)



# a = 'aannaa'
# n = len(a)
# polydrome = True
# for i in range(int(n)):
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         polydrome = False
# print(polydrome)




# a = 121
# n = len(a)
# b = n//2
# c = 0
# palendrome = True
# for i in range(a):
#     c = i+1
#     print(c)
#     if a[n-1-i]==a[i]:
#         pass
#     else:
#         palendrome = False
#         break
# print(palendrome)



# a = 'kdkdkdkdkdk'
# n = len(a)
# palendrome = True
# c = 0
# for i in range(n//2):
#     c = c+1
#     if a[i]==a[n-1-i]:
#         pass
#     else:
#         palendrome = False
# print(palendrome)
# print(c)



# a = 'kdkdkdkdkdk'
# n = len(a)
# i = 0
# palendrome = True
# while (n>i):
#     a[i]==a[n-1-i]
#     pass
# else:
#     palendrome = False
# print(palendrome)




# a = 'kdkdkdkdkdk'
# n = len(a)
# palendrome = True
# c = 0
# for i in range(n//2):
#     c = c+1
#     if a[i]==a[n-1-i]:
#         pass
#     else:
#         palendrome = False
# print(palendrome)
# print(c)


# a = 121
# b = a
# c = 0
# while b>0:
#     rem = b%10
#     c = c*10+rem
#     b = b//10
#     if a==c:
#         print('yes')
#     else:
#         print('no')    


# a = 'hello i am data scientist'
# def extract_first_letter (a):
#     '''this is extract first letter'''
#     a  = a.split(' ')
#     first_letter_list = []
#     for i in range(a):
#         first_letter_list.append(a[i][0])

#         return first_letter_list

#         print(first_letter_list)


