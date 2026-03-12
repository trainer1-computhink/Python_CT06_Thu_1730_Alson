# Recap 1
# total = 1
# for i in range(1, 6):
#     number = int(input("What is number #" + str(i) + "? "))
#     total = total * number
# print("Total: " + str(total))

# Task 1
# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# Task 2a
# import random

# random_num = random.randint(1, 6)
# print(random_num)

# Task 2b
# import random

# for i in range(20):
#     random_num = random.randint(0, 9999)
#     print(random_num)

# Task 4
# import random

# random_num = random.randint(1, 10)
# guess = int(input("Guess the random number: "))

# if guess == random_num:
#     print("Correct!")
# else:
#     print("Wrong!")

# Task 5
# import random

# random_num1 = random.randint(1, 50)
# random_num2 = random.randint(1, 50)
# answer = random_num1 + random_num2

# user_answer = int(input("What is " + str(random_num1) + " + " + str(random_num2) + "?\n"))

# if user_answer == answer:
#     print("Correct!")
# else:
#     print("Wrong!")

# Task 6
# import random

# num_questions = int(input("How many questions would you like?\n"))

# for i in range(num_questions):
#     random_num1 = random.randint(1, 10)
#     random_num2 = random.randint(1, 10)
#     answer = random_num1 * random_num2

#     user_answer = int(input("What is " + str(random_num1) + " x " + str(random_num2) + "?\n"))

#     if user_answer == answer:
#         print("Correct!")
#     else:
#         print("Wrong!")

# Task 7
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Task 8
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if number2 % number1 == 0:
    print("True")
else:
    print("False")