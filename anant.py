# secret_word = "anant"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#        guess = input("enter guess:")
#        guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("you lose")

# else:
#     print("you win")



# secret_word = "anant"
# guess = ""
# guess_count = 1
# guess_limit = 3
# flag = False

# while guess_count <= guess_limit:
#     guess = input("enter guess:")
#     if guess == secret_word:
#         flag=True
#         break
#     guess_count += 1   
       
# if flag:
#     print("you win")
# else:
#     print("you loose")



# for x in "anant":
#   print(x)


# for x in range(2 , 10):
#   print(x)


# number_grid = [
#     [1 , 2 , 3],
#     [4 , 5 , 6],
#     [7 , 8 , 9],
# ]

# print(number_grid[2][2])

# for x in number_grid:
#     print(x)



# def converttopaise(txt):
#    if txt.isnumeric():
#        rupees= int(txt) 
#        return rupees*100
#    else:
#        return False


# txt = input("enter the number : ")
# result = converttopaise(txt)

# if result:
#     print(result)

# else:
#     print("invalid num")


# rupees = float(input("enter any number :"))

# result = rupees*100

# print(result)



# principle = float(input("enter principle :"))
# rate = float(input("enter rate :"))
# time = float(input("enter time :"))

# result = (principle*rate*time)/100

# print(result)



# def converttopaise(txt):
#    return txt * 100

# try:
#     txt = int(input("enter the number : "))
#     result = int(converttopaise(txt))
#     print(result)
# except: 
#     print("number not valid")







# def simpleinterest(txt):
#     return txt

# try:
#     principle=int(input("enter principle :"))
#     rate=float(input("ente rate :"))
#     time=int(input("enter time :"))
#     txt=(principle*rate*time)/100
#     result=float(simpleinterest(txt))
#     print(result)
    
# except:
#     print("invalid")










# # def divide(txt):
# #     return txt

# # try:
# #     numerator=int(input("enter numerator :"))
# #     denominator=int(input("enter denominator :"))
# #     quotient=int(numerator/denominator)
# #     reminder=int(numerator%denominator)
# #     txt=('quotient' , 'reminder')
# #     result=int(divide(txt))
# #     print(result)
    
# # except:
# #     print("invalid")

# /


# import math

# num = 11

# print(math.ceil(num / 2))

# for i in range(2 , math.ceil(5.5)):
#      print(i)
# num = int(input("enter any number :"))

# if num > 1:
#     for i in range(2 , int(num / 2)):
#         if (num % i) ==  0:
#             print(num , "is not prime number")
#             break
#     else:
#             print(num , "is prime number")
            
# else:
#     print(num , "is not a prime number")            








# def is_prime(number):
#     if number > 1:
#         for i in range(2 , int(number / 2)+1):
#             if (number % i)== 0:
#               print("the number is not prime")
#               break
#         else:
#             print("the number is prime")

# number = int(input("Enter any number :"))
# is_prime(number)






# num1 = int(input("enter any num :"))
# num2 = int(input("enter anathor num :"))


# try:
#     result = num1 / num2

# except:
#     print(f'{num1} is not divisible by 0')

# else:
#     print(f'{num1}is divided by{num2}is {result}')









# num1 = int(input("enter any num :"))
# num2 = int(input("enter anathor num :"))


# for i in range(num1 , num2):
#     if (i % 2)==0:
#         print(i)





# def is_prime(number1 , number2):
#   for number in range(number1 , number2+1):
#     if number > 1:
#         for i in range(2 , int(number / 2)+1):

#             if (number % i)== 0:
#             #  print("the number is not prime")
#              break
#         else:
#             print(number)



# number1 = int(input("Enter any number :"))
# number2 = int(input("Enter another number :"))
# is_prime(number1 , number2)





# p = int(input("enter any value :"))
# count = 0
# n = 1

# while count < p:
#     ele = 5*n+2
#     if((ele%4)==0):
#         continue
#     else:
#         count += 1
#         n+=1
#     print(ele)








# def areaOfRhombus(diagonal1, diagonal2) :
# 	ans = diagonal1 // 2 * diagonal2

# #main
# string = input().strip().split(' ')
# diagonal1 = int(string[0])
# diagonal2 = int(string[1])

# ans = areaOfRhombus(diagonal1, diagonal2)

# print(ans)
x = 3.5
print(float(int(x)))

