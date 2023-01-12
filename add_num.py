#!/usr/bin/python3
two_digits = input('Enter a 2 digit number\n')
digit_1 = two_digits[0]
digit_2 = two_digits[1]

# convert string data type to respective data types /int and floata
new_digit1 = int(digit_1)
new_digit2 = int(digit_2)
num_sum = new_digit1 + new_digit2
print(num_sum)
