# Qualynn McDowell
# November 6, 2026
# P4HW1
# Average score grade list with letter grades

# ----------------------------------------------------------------------------
# Ask user for number of scores they want to enter
# ----------------------------------------------------------------------------
num_scores = int(input("Enter the number of scores you want to enter: "))
print()

score_list = []

# ----------------------------------------------------------------------------
# Loop to collect and validate scores
# ----------------------------------------------------------------------------
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score {i}: "))

    # Input validation loop
    while score < 0 or score > 100:
        print("\nINVALID SCORE ENTERED!!! ")
        print("Should be between 0 and 100.")
        score = float(input(f"Enter score #{i} again: "))

    # Add valid score to the list
    score_list.append(score)

# ----------------------------------------------------------------------------
# Process scores
# ----------------------------------------------------------------------------
lowest_score = min(score_list)

# Copy original list and drop lowest score
modified_scores = score_list.copy()
modified_scores.remove(lowest_score)

average = sum(modified_scores) / len(modified_scores)

# ----------------------------------------------------------------------------
# Determine letter grade based on average
# ----------------------------------------------------------------------------
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# ----------------------------------------------------------------------------
# Display results
# ----------------------------------------------------------------------------
print("\n" + "-------------------ReSults-------------------")
print(f"{'Lowest Score' :<18}: {lowest_score}")
print(f"{'Modified List' :<18}: {modified_scores}")
print(f"{'Score Average' :<18}: {average:.2f}")
print(f"{'Grade' :<18}: {letter_grade}")
print("---------------------------------------------")