#!/usr/bin/python3
# This program checks body mass index and and
# interprets the results
# íº¨ Don't change the code below í±‡
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# íº¨ Don't change the code above í±†

#Write your code below this line í±‡
body_mass_index = weight/height ** 2

if body_mass_index < 18.5:
    print(f"Your BMI is {round(body_mass_index)}, you are underweight.")
elif body_mass_index > 18.5 and body_mass_index < 25:
    print(f"Your BMI is {round(body_mass_index)}, you have a normal weight.")
elif body_mass_index > 25 and body_mass_index < 30:
    print(f"Your BMI is {round(body_mass_index)}, you are slightly overweight.")
elif body_mass_index > 30 and body_mass_index < 35:
    print(f"Your BMI is {round(body_mass_index)}, you are obese.")
else:
    print(f"Your BMI is {round(body_mass_index)}, you are clinically obese.")
