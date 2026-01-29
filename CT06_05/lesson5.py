# name = "John"   # String
# age = 10        # Integers
# weight = 50.5   # Float

# # Data Types

# a = "10"
# b = 10

# # Type Casting
# a = int(a)
# c = a + b
# print(c)

# # String Concatenation 
# name = "John"
# surname = "Smith"
# print(name + " " + surname)

# Recap 1
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# message = input("Enter your message: ")

# # String concatenation
# print("Happy " + age + "th birthday " + name + "! " + message)
# # f-string (formatted string)
# print(f"Happy {age}th birthday {name}! {message}")

# Task 1
# for i in range(100):
#     print("I like chicken rice.")

# Task 2
# for i in range(100):
#     print("I like cake,")
#     print("give me more!")

# # Task 3
# for i in range(0, 60, 1):
#     print(i)

# # Task 4
# for i in range(1, 6):
#     print(i)

# for i in range(51, 101):
#     print(i)

# for i in range(18, 30):
#     print(i)

# # Task 5
# for i in range(2, 25, 2):
#     print(i)
    
# for i in range(8, 97, 8):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# Task 6
# print("Ready!")
# for i in range(3, 0, -1):
# 	print(i)

# Task 7
# start = input("Enter start number: ")
# start = int(start) # Casting to convert string to integer
# stop = input("Enter stop number: ")
# stop = int(stop) # Casting to convert string to integer

# for i in range(start, stop + 1):
#     print(i)

# total = start + stop
# print(total)

# total = 0
# for i in range(10):
#     total = total + 2
#     # 1st -> 0 = 0 + 2
#     # 2nd -> 2 = 2 + 2
#     # 3rd -> 4 = 4 + 2
#     # 4th -> 6 = 6 + 2
#     # ...
# print(total)

# Task 8a
# total = 0
# for i in range(2, 41, 2):
#     total = total + i
# print(total)

# word = "ABCDEFGHIJK"
# for char in word:
#     print(char)

# Task 9
name = input("Enter your name: ")
for char in name:
    print("Give me a " + char + "!")
print("What do we have?")
print(name + " is the best!")