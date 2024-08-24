# a= "hello i m anant,"
# b= 22
# print(a + str(b))


# def max_num(num1 , num2 , num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(22 , 34 , 21))        


# num1 = float(input("enter a number:"))
# op   = input("enter operator:")
# num2 = float(input("enter second number:"))
# if op == "+":
#    print(num1 + num2)
# elif op == "-":
#    print(num1 - num2)
# elif op == "/":
#    print(num1 / num2)  
# elif op == "*" :
#    print(num1 * num2) 
# else:
#     print("invalid")        




# i= 1
# while i <= 10:
#     print(i)
#     i = i + 1

# print("done with loop") 


secret_word = "anant"
guess = ""
guess_count = 0
guess_limit = 3
while guess != secret_word:
    guess = input("enter guess: ")
    guess_count += 1

print("you win!")