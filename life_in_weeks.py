#!/usr/bin/python3
# � Don't change the code below �
age = input("What is your current age?\n")
life_expectancy = input("How many years in total do you expect to live?\n")
# � Don't change the code above �

#Write your code below this line �
years_left = int(life_expectancy) - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

if int(life_expectancy) < 100:
    print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
else:
    print("Over 100 years is unrealistic. Come on man!")
