# Qualynn McDowell
# October 5, 2026
# P2HW1
# This program calculates and displays travel expenses.

# Calculating Travel Expenses

print("This program calculates and displays travel expenses.")
print()

budget = float(input("Enter Budget: ")) 
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

print('----------Travel Expenses----------')
print(f"{'Location:' :<20} {destination}")
print(f"{'Initial Budget:' :<20} ${budget:.2f}")
print(f"{'Fuel:' :<20} ${gas:.2f}")
print(f"{'Accommodation:' :<20} ${accommodation:.2f}")
print(f"{'Food:' :<20} ${food:.2f}")
print('-----------------------------------')

expenses = (gas + accommodation + food)
final_budget = budget - expenses
print("Remaining Balance:", final_budget)

