# Recap 1
# balance = 1000
# while True:
#     print("--- Welcome to the ATM ---\n")
#     print(f"Current balance : ${balance}\n")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Check Balance")
#     print("4. Exit\n")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         withdraw_amount = input("Enter the amount you want to withdraw: ")

#         if not withdraw_amount.isdigit():     
#             print("\nInvalid amount. Please try again.\n")
#             continue
#         else:
#             if int(withdraw_amount) <= balance:
#                 print(f"\nYou have withdrawn ${withdraw_amount}.\n")
#                 balance -= int(withdraw_amount)
#             else:
#                 print(f"\nYou cannot withdraw more than ${balance}.\nPlease try again.\n")
#                 continue
#     elif choice == "2":
#         deposit_amount = input("Enter deposit amount: ")
#         if not deposit_amount.isdigit():     
#             print("\nInvalid amount. Please try again.\n")
#             continue
#         else:
#             balance += int(deposit_amount)
#             print(f"\nYou have deposited ${deposit_amount}.\n")
#     elif choice == "3":
#         print(f"\nCurrent balance: ${balance}\n")
#     elif choice == "4":
#         print("\nThank you for banking at this ATM.\nHave a nice day!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# Task 1
# groceries = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey"
# ]

# groceries[7] = "Herbs"
# # print(groceries)

# # for item in groceries:
# #     print(item)

# # for i in range(len(groceries)):
# #     print(groceries[i])

# # Add at a certain index
# groceries.insert(1, "Bananas")
# print(groceries)

# # Add to the end
# groceries.append("Ice")
# print(groceries)

# # del(groceries[2])
# removed = groceries.pop(2)
# print(groceries)
# print(f"{removed} was removed.")

# # Task 2
# for i in range(len(groceries)):  
#     if groceries[i] == "Apples":
#         print(f"{groceries[i]}: I will need 5 of these")
#     elif groceries[i] == "Carrots":
#         print(f"{groceries[i]}: I will need 3 of these")
#     elif groceries[i] == "Grapes":
#         print(f"{groceries[i]}: Get the FarmFresh brand")
#     else:
#         print(groceries[i])

# Task 3
groceries = []
while True:
    item = input("What item have you added to your basket?\n")
    if item == "end":
        break
    groceries.append(item)
    
for i in range(len(groceries)):
    print(f"I have bought {groceries[i]}.")

# Task 4
# num = 0
# while num < 10:
#     num += 1
#     print(num)

# while True:
#     if num == 10:
#         break