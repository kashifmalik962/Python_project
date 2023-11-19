# from threading import Thread

# def disp():
#     for i in range(5):
#         print('Thread running')

# t = Thread(target=disp)
# t.start()


# for i in range(5):
#     print('Main Thread')



# from threading import Thread

# t = Thread()
# print(t.name)



                        # Creating a Thread by creating Child Class to Thread Class



# from threading import Thread

# class Mythread(Thread):
    
#     def run(self):
#         for i in range(5):
#             print('Child Method')

# t = Mythread()
# t.start()
# t.join()

# for i in range(5):
#     print('Main Thread')



                        # Thread Child Class with Constructor


# from threading import Thread

# class Mythread(Thread):
    
#     def __init__(self,a):
#         Thread.__init__(self)
#         print('Child class constructur', a)

#     def run(self):
#         pass
# t = Mythread(10)
# t.start()




