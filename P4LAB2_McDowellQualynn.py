# Qualynn McDowell
# November 6, 2026
# P4LAB2
# Use while loop and for loop together

'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, repeat program
If no, exit program
'''

run_again = 'yes'

while run_again != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        # Display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} x {item} = {user_num * item}")
    else:
        print("Program cannot accept negative numbers.")
    
    run_again = input("Would you like to run the program again? ")

# Loop has broken. User entered 'no'
print('Program has ended.')