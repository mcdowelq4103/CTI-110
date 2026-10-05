# Qualynn McDowell
# October 4, 2026
# P2LAB1
# Code that performs mathematical calculations and displays information to users

# Import the math module to use the constant, math.pi
import math

# Get the radius from the user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate the diameter of the circle
diameter = 2 * radius

# Display the diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calculate the circumference of the circle
circumference = 2 * math.pi * radius

# Display the circumference with 2 decimal point
print(f"The circumference of the circle is {circumference:.2f}\n")

# Calculate the area of the circle
area = math.pi * radius ** 2

# Display the area with 3 decimal point
print(f"The area of the circle is {area:.3f}\n")
