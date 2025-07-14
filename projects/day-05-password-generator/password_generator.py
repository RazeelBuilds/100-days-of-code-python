import random

# Define possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Greet the user
print("Welcome to the PyPassword Generator!")

# Get the desired count of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ------------------ VERSION 1 (Simple but less secure shuffle) ------------------
# password = ""
#
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#     random.shuffle(password)
# print(password)

# ------------------ VERSION 2 (Using list and shuffle) ------------------

# Store characters in a list to allow shuffling
password_list = []

# Add random letters
for char in range(0, nr_letters):
    password_list.append (random.choice(letters))

# Add random symbols
for char in range(0, nr_symbols):
    password_list.append (random.choice(symbols))

# Add random numbers
for char in range(0, nr_numbers):
    password_list.append (random.choice(numbers))

# Print the list before shuffling (optional debug)
print(password_list)

# Shuffle the password list to randomize order
random.shuffle(password_list)

# Print the list after shuffling (optional debug)
print(password_list)

# Convert the list into a single string by adding each character one by one
password = ""
for char in password_list:
    password += char

# Display the final password
print(f"Your Password is: {password}")
