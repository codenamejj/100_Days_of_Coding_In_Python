#!/usr/bin/python3
# This code below has been modified to take more inputs.
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?\n$")
tip_percentage = input("What tip percentage would you like to give?\n")
num_people = input("How many people are splitting the bill?\n")

split_bill = (float(total_bill) / int(num_people)) *\
                       ((100 + float(tip_percentage)) / 100)
split_bill_convert = float(round(split_bill, 2))
print(f"Each person should pay: ${split_bill_convert}")
