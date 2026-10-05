# Qualynn McDowell
# October 5, 2026
# P2LAB2
# Using dictionary to store and display user input

cars = {"Camaro":18.2, "Prius":52.36, "Model S": 110, "Silverado": 26 }

#Get keys from the dictionary
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep=", ")

# Get a car from user
car_name = input("Enter the name of the car: ")

# Get mpg for the selected car
car_mpg = cars[car_name]
print(f"The MPG for {car_name} is {car_mpg} miles per gallon.") 

# Get miles driven from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

# Calculate gallons used
gallons_needed = miles_driven / car_mpg

# Display results
print(f"To drive {miles_driven} miles, the {car_name} will use {gallons_needed:.2f} gallons of fuel.")
