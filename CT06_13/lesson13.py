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
groceries = [
    "Bread",
    "Milk",
    "Eggs",
    "Potato Chips",
    "Fruits",
    "Ice Cream",
    "Tea",
    "Coffee"
]

groceries[7] = "Banana"
# print(groceries)

# for item in groceries:
#     print(item)

# for i in range(len(groceries)):
#     print(groceries[i])

# Add at a certain index
groceries.insert(1, "Apple")
print(groceries)

# Add to the end
groceries.append("Peanuts")
print(groceries)

del(groceries[0])
removed = groceries.pop(5)
print(groceries)
print(removed)