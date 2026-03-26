# Recap 1
import random

random_num = random.randint(1, 15)

guess = int(input("Enter your guess: "))
if guess == random_num:
    print("That's it!")

print(random_num)

# Task 1
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number == 0:
    print(f"{number} is neutral.")
else:
    print(f"{number} is negative.")

# Task 2
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
else:
    if age >= 13 and age <= 19:
        print("Teen")
    else:
        print("Adult")

# Task 3
temperature = input("Enter the temperature: ")

if temperature > 30:
    print("Go swimming.")
elif temperature >= 25:
    print("Play basketball.")
elif temperature >= 20:
    print("Go cycling.")
else:
    print("Read indoors.")

# Task 4
score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Task 5
age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# Task 6
monies = int(input("How much money do you have?\n"))

if monies >= 150:
    print("Buy a gaming keyboard.")
elif monies >= 100:
    print("Buy a new video game.")
elif monies >= 50:
    print("Buy a new gaming mouse.")
elif monies >= 20:
    print("Buy a new mouse pad.")
else:
    print("Buy some snacks.")