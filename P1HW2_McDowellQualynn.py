# Qualynn McDowell
# September 24, 2026
# P1HW2
#calculating and displaying travel expenses

# Calculating Travel Expenses

print("Calculating Travel Expenses")
print()

budget = float(input("What is your total travel budget? ")) 
destination = input("Where are you traveling to? ")
gas = float(input("How much do you plan to spend on gas? "))
accommodation = float(input("How much do you plan to spend on accommodation? "))
food = float(input("How much do you plan to spend on food? "))

print('----------Travel Expenses Summary----------')
print("Location: ", destination)
print("Initial Budget: $", budget)
print()
print("  - Gas: $", gas)
print("  - Accommodation: $", accommodation)
print("  - Food: $", food)

expenses = (gas + accommodation + food)
final_budget = budget - expenses
print("Remaining Balance:", final_budget)