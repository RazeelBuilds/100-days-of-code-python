# Day 01 - Band Name Generator Project
# Project: Generate a fun band name by combining the name of the city you grew up in and your pet's name.
# Skills Practiced: Using input(), string concatenation, and formatted output with print().

# 1. Display a welcome message to the user
print("Welcome to the Band Name Generator.")

# 2. Ask the user for the name of the city they grew up in
city = input("What's the name of the city you grew up in?\n")

# 3. Ask the user for their pet's name
pet = input("What's your pet's name?\n")

# 4. Combine city and pet name to create a band name
band_name = city + " " + pet

# 5. Display the generated band name
print("Your band name could be " + band_name)
