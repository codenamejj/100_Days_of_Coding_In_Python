#!/usr/bin/python3
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

body_mass_index = float(weight)/(float(height) ** 2)
print(int(body_mass_index))
