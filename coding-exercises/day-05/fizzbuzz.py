# FizzBuzz Exercise - Day 05 of 100 Days of Code

# Create a loop with For and Range to go from 1 to 100.
for number in range(1, 101):
# First check if the number is divisible by both 3 and 5, print "FizzBuzz"
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
# Then check if the number is only divisible by 3, print "Fizz"
    elif number % 3 == 0:
        print("Fizz")
# Finally check if the number is only divisible by 5, print "Buzz"
    elif number % 5 == 0:
        print("Buzz")
# If it's not divisible by either of those numbers, print the number itself
    else:
        print(number)
