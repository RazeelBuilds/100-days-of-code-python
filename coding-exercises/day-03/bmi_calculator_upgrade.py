# Day 03 - BMI Calculator with Interpretations
# Task: Use if else and elif to upgrade the BMI calculator to give interpretations.
# Goal: To practice using control flow  (if, elif, and else) and logical operaters in Python
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >=18.5:
    print("normal weight")
else: 
    print("underweight")
