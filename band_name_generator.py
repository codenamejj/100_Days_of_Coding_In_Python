#!/usr/bin/python3
print("Welcome to the Band Name Generator.")
town_name = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

band_name = town_name + " " + pet
print('Your band name could be: {}'.format(band_name), end="")
print()
