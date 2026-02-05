# Recap 1
# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score) + ".")

# # f-string = formatted string
# print(f"Average score for {student_name} is: {average_score}.")

# Task 1
# for i in range(1, 11):
#     print(i)

# Task 2
# for i in range(2, 21, 2):
#     print(i)

# Task 3
# for i in range(10, 0 , -1):
#     print(i)

# Task 4
# word = input("Enter a word to repeat: ")
# num = int(input("How many times to repeat: "))

# for i in range(num):
#     print(word)

# Task 5
# name = input("Enter a name to repeat: ")
# num = int(input("How many times to repeat: "))

# for i in range(num):
#     print(f"Nice to meet you, {name}.")

# Task 6
# total = 0
# for i in range(5):
#     number = int(input(f"What is number #{i + 1}? "))
#     total = total + number

# print(f"Sum of the 5 numbers is {total}.")

# Task 7
number = int(input("Which number's timetable to print? "))
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")