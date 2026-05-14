# Recap 1
# import random

# rolls = []

# for i in range(5):  
#     rolls.append(random.randint(1, 6))

# print(rolls)

# total = 0

# for i in range(len(rolls)):
#     total += rolls[i]

# print(f"Sum: {total}")

# Task 1
# fruits = ["Apple", "Banana", "Cherry", "Durian"]
# price = [2, 3, 5, 10]

# for i in range(len(fruits)):
#     print(f"{fruits[i]} costs ${price[i]}")

# Task 2
# items = ["Apple", "Milk", "Bread", "Egg", "Chocolate"]
# stock = [15, 0, 8, 25, 3]

# for i in range(len(items)):
#     if stock[i] >= 10:
#         status = "Well Stocked"
#     elif stock[i] < 10 and stock[i] > 0:
#         status = "Low Stock"
#     else:
#         status = "Out of Stock"
#     print(f"Item: {items[i]} | Qty: {stock[i]} | Status: {status}")

# ask = input("Check stock for which item?\n")

# if ask in items:
#     item_index = items.index(ask)
#     print(f"We have {stock[item_index]} {ask}(s) remaining.")
# else:
#     print(f"Error. {ask} is not in the database.")

# Task 4
import random

moves = ["scissors", "paper", "stone"]
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player_move = input("Pick scissors, paper or stone: ")
    computer_move = random.choice(moves)
    print(f"Computer chose {computer_move}.")

    if player_move == computer_move:
        print("It's a draw!")
    elif (player_move == "scissors" and computer_move == "paper") or (player_move == "paper" and computer_move == "stone") or (player_move == "stone" and computer_move == "scissors"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1 
    print(f"Score - You: {player_score} | Computer: {computer_score}")

if player_score == 3:
    print("Game Over! You beat the Computer!")
else:
    print("Game Over! You lost to the Computer!")