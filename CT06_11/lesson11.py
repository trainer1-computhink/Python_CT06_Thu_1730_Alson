# Recap 1
# px = int(input("What is the price of the item? "))

# if px <= 5:
#     print("Sounds good!")
# elif px <= 50:
#     print("Are you sure you need this?")
# elif px <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")

# Task 1
# rider1 = 125
# rider2 = 150

# if rider1 > 120 and rider2 > 120:
#     print("You can ride.")
# else:
#     print("You must leave.")

# Task 2
# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 7 == 0:
#     print("This number is divisible by 3 and 7.")

# Task 3
# first_name = input("Enter your first name: ").lower()
# last_name = input("Enter your last name: ").lower()

# if first_name == "james" and last_name == "leong":
#     print("YOU ARE WANTED!")

# Task 4
# rider1 = 25
# rider2 = 6

# if rider1 >= 18 or rider2 >= 18:
#     print("You are allowed to ride.")

# Task 5
# age = int(input("Enter your age: "))

# if age < 12 or age > 65:
#     print("Your ticket is $15.")
# else:
#     print("Your ticket is $20.")

# Task 6
# gender = input("Enter your gender: ").lower()

# if gender == "m" or gender == "male":
#     print("Valid Input")
# else:
#     print("Invalid Input")

# Task 7
# colour = input("Enter a colour: ").lower()

# if not colour == "green":
#     print("Try Again")

# Task 8
# day = input("Enter day of week: ").lower()

# if not day == "saturday" or not day == "sunday":
#     print("It is not the weekend.")

# Task 10
# want_burger = input("Do you want a burger? (Yes/No) ").lower() == "yes"
# want_drink = input("Do you want a drink? (Yes/No) ").lower() == "yes"
# want_fries = input("Do you want fries? (Yes/No) ").lower() == "yes"

# if want_burger and want_fries and not want_drink:
#     print("Won't you get thirsty?")

# Task 11
# stored_username = "John123"
# stored_password = "pw123"

# entered_username = input("Enter your username: ")
# entered_password = input("Enter your password: ")

# if entered_username == stored_username and entered_password == stored_password:
#     print("Access Granted")
# elif entered_username == stored_username or entered_password == stored_password:
#     print("Either username or password is incorrect")
# else:
#     print("Access Denied")

# Task 12
# game_status = "active"

# if game_status == "active" or not game_status == "paused":
#     print("Game in progress...")
# else:
#     print("Game is paused or inactive.")