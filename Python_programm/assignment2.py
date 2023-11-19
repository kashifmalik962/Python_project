                                # AMONG THREE NUMBER

# def among(a,b,c):
#     a,b,c = a,b,c
    
#     if a < b:
#         if a < c:
#             return a
        
#     if b < a:
#         if b < c:
#             return b
    

#     if c < a:
#         if c < b:
#             return c

# print(among(40,0,60))


                            # PALINDROOME



# def is_palindrome(number):
#     original_num = number
    
#     reverse_num = 0
#     while number > 0:
#         remainder = number % 10
#         reverse_num = (reverse_num * 10) + remainder
#         number = number // 10
    
    
#     if original_num == reverse_num:
#         return True
#     else:
#         return False

# print(is_palindrome(12121))



                        # ARMSTRONG NUMBER


# def is_armstrong_number(number):

#   digits = list(str(number))
#   sum_of_cubes = 0
#   for digit in digits:
#     sum_of_cubes += int(digit) ** 3

#   return number == sum_of_cubes

# print(is_armstrong_number(372))