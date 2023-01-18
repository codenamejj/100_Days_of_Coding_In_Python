#!/usr/bin/python3
import random
# this function will print one list name at random
# we are not using the choice() function
# say we have a list saved in variable 'numbers'

numbers = ['Good', 'stories', 'are', 'easy', 'to', 'tell']
# we want our function to choose from the list at random
# just like the choice() function does
# finding lenght of list with for loop
# use the lenght to determine the last list index = list(list_lenght- 1)
# we can manipulate/ randomize the index for us to randomize the choices
# of our list
list_len = 0
for word in numbers:
    list_len += 1
    last_list_index = list_len - 1
    rand_index = random.randint(0, last_list_index)
print(f"Your list is: {numbers}")
print(f"Your random list index is: {rand_index}")
print(f"Your random list choice is: {numbers[rand_index]}")
