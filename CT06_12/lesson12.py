# Recap 1
# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by 3 and 5!")
# else:
#     print(f"{num} is not divisible by 3 and 5!")

# Task 1
# visitors = 4
# max_visitors = 25
# while visitors < max_visitors:
#     visitors += 1
#     print(visitors)

# Task 2
# visitors = 0
# while True:
#     visitors += 1
#     print(visitors)

#     # Stop and exit loop
#     if visitors == 30:
#         break

# Task 3
# Initialize
# order = input("Enter your order: ")
# while True:
# 	new_order = input("Enter your order: ")
# 	if new_order == "end":
# 		break
# 	order += ", " + new_order
# print(order)

# Task 4
# num = 10

# while num != 0:
#     print(num)
#     num -= 1

#     # if num == 5:
#     #     break
# else:
#     print("Happy New Year!")

# Task 5
import random

score = 0
correct_answers = 0
while True:
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.randint(1, 3)
    if operation == 1:
        ans = num1 + num2
        operation_sign = "+"
    elif operation == 2:
        ans = num1 - num2
        operation_sign = "-"
    else:
        ans = num1 * num2
        operation_sign = "x"

    user_ans = input(f"What is {num1} {operation_sign} {num2}?\n")

    if int(user_ans) == ans:
        print(f"That's correct!")
        correct_answers += 1
        score += 2
        if correct_answers == 5:
            print(f"You scored: {score}")
            break
    else:
        print("That's wrong! Try again.")
        score -= 1