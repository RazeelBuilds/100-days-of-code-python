# Day 02 – Tip Calculator Project
# Project: Calculate how much each person should pay after splitting a bill, including tip.
# Skills Practiced: Using input(), float/int conversion, arithmetic operations, and round() function

print("Welcome to the tip calculator!")


# Get the total bill amount from the user
bill = float(input("What is the total bill? $"))

# Ask the user what percentage tip they want to give
tip = int(input("What percentage would you like to give as a tip? 10, 12, 15? "))

# Calculate the total bill including tip
total_bill = tip / 100 * bill + bill
print(f"Your total bill with the tip is: ${round(total_bill,2)}")

# Ask how many people are splitting the bill
people = int(input("How many people will be splitting the bill? "))

# Calculate the amount each person should pay
per_person_split = total_bill / people
print(f"The amount each person should pay is: ${round(per_person_split,2)}")


# Example:
# Input: bill = 150, tip = 10, people = 5
# Output: $33.0
