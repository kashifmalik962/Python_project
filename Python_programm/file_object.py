# Open the file in write mode.

# f = open('student.txt', mode='w')
# f.write('hello kashif')
# f.close()



# f = open('student.txt', mode='a')
# f.write('hello kashif anas')
# f.close()



# f = open('student.txt', mode='w')
# lst = ('kashif ', ' anas ', ' aahad ', ' salman ', ' danish ', ' javed ')
# f.writelines(lst)
# f.close()


                      # THIS X METHOD IS FIRST CREATE A FILE AND THEN WRITE

# f = open('student.txt', mode='x')
# f.write('hello kashif')
# f.close()




# f = open('student.txt', mode='r')
# data = f.read(10)
# print(data)


                                # r+ w+ a+


f = open('student.txt', 'r+')
data = f.read()
f.write('youtube')
print(data)