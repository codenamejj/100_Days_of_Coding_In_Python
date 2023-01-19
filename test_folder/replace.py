#!/usr/bin/python3
import random
print("Welcome to the z-guess game!")
animal_list = ["Elephant", "rhino", "lion", "cow", "zebra", "chicken", "dog"]
random_animal = random.choice(animal_list)

blanks = []
for check in random_animal:
    blanks += ["_"]
# print(blanks)

end_game = False
while not end_game:
    print(blanks)
    guess = input("Guess a letter.\nHint: animal name\n").lower()
    word_len = len(random_animal)
    for index in range(word_len):
        letter = random_animal[index]
        if guess == letter:
            blanks[index] = letter
    if "_" not in blanks:
        end_game = True
#        print(blanks)
    word = ""
    for char in blanks:
        word += char
    print(word)
