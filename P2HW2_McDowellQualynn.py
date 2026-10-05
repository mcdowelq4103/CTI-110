# Qualynn McDowell
# October 5, 2026
# P2HW2
# This program will assess student understanding of Lists

# Calculate the average, lowest, highest, and sum of six grades entered by the user.

# Ask the user to enter the grade for each module.
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store all six grades in a list.
grades = [module1, module2, module3, module4, module5, module6]

# Find the lowest grade in the list.
lowest_grade = min(grades)
# Find the highest grade in the list.
highest_grade = max(grades)
# Find the sum of the grades in the list.
total_grades = sum(grades)
# Find the average of the grades.
average_grade = total_grades / 6

# Display the results.
print()
print("------------Results------------")
print(f"{'Lowest Grade: ' :<20} {lowest_grade}")
print(f"{'Highest Grade: ' :<20} {highest_grade}")
print(f"{'Sum of Grades: ' :<20} {total_grades}")
print(f"{'Average: ' :<20} {average_grade:.2f}")