# for i in range(10):
#     if i%2==0:
#         if i%3==0:
#             print(i)
    

# a = []
# for i in range(50):
#     a.append(i+1)
# print(a)

# a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# b = [i+1 for i in a]
# print(b)



# b = [i+1 for i in range(50)]
# print(b)


# a = [i for i in range(20) if i%2==0]
# print(a)


# a = [i for i in range(20) if i%2==0 if i%3==0]
# print(a)


# a = []
# for i in range(20):
#     if i%2==0:
#         a.append(i)
#     else:
#         a.append('invalid')
# print(a)


# a = [i if i%3==0 else 'invalid' for i in range(20)]
# print(a)



# a = [i if i%3==0 else 'invalid' for i in range(20)]
# print(a)
# print(a.count('invalid'))


# a = [i  if i%3==0 else "invalid" for i in range(10)]
# print(a)


# for i in range(10):
#     if i%2==0:
#         print(i)
#     else:  
#         print('invalid')


# for i in range(6,8):
#     for a in range(8,10):
#         print(i*a)


# for i in range(3):
#     print(i)
#     for a in range(2):
#         print(a)

# a = [a*i for i in range(3) for a in range(2)]
# print(a)




# a = [i if i%2==0 if i%3==0 else "Invalid" for i in range(10)]
# print(a)



# for i in range(10):
#     if i%2==0:
#         if i%3==0:
#             print(i)
#     else :
#         print('Invalid')


# a = [i  for i in range(10)]



# a = {i if i%2==0 else "Invalid" for i in range(10)}
# print(a)


# a = [(i,a) for i in range(2) for a in range(4,6)]
# print(a)


# a = {(i,a) for i in range(3) for a in range(2)}
# print(a)



# a = {(i,a) for i in range(2) for a in range(4,6)}
# print(a)



# a = {i if i%2==0 and i%3==0 else "invalid" for i in range(10)}
# print(a)


# a = {(i,a) for i in range(2) for a in range(3,5)}
# print(a)


# a = [(i,a) for i in range(2) for a in range(3,5)]
# print(a)



# a = {(i,a) for i in range(2) for a in range(3,5)}
# print(a)

# even = [n for n in numbers if 0 == n % 2 and break if n == 412]


# for i in range(10):
#     if i==6:
#         break
#     print(i)



# a = {"kas":'kashif'}
# print(a['kas'])
# print(type(a))


# a = {}
# for i in range(10):
#     a[i]=i*5
# print(a)



# a = {i:i*2  if i%2==0 and i%3==0 else "Invalid" for i in range(10)}
# print(a)


# dic = {101:"kashif",102:"anas",103:"salman"}
# tup = dic.items()

# dict = {k:v for k,v in tup}
# print(dict)



# a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in a:
#     if i=='a':
#         print('vovel')
#     if i=='e':
#         print('vovel')
#     if i=='i':
#         print('vovel')
#     if i=='o':
#         print('vovel')
#     if i=='u':
#         print('vovel')
# else:            
#     print('consonenent')



# b = []
# c = []
# a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in a:
#     if i == 'a':
#         a.append(i)
#     if i == 'e':
#         a.append(i)
#     if i == 'i':
#         a.append(i)
#     if i == 'o':
#         a.append(i)    
#     if i == 'u':
#         a.append(i)
#     else:
#         c.append(c)
# print(b)
# print(c) 

# a = 11
# b = 18
# c = []
# c = a
# a = b
# b = c
# for i in a:
    


# a = [[50,60],[40,90]]
# print(sorted(a))



# a = 'kashif'
# print('sa' in a)



dic = {101:"kashif",102:"anas",103:"salman"}
print('kashif' in dic)