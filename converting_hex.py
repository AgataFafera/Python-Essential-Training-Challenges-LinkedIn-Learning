#!/usr/bin/env python
# coding: utf-8


hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None

def hex_function(num):
    for i in num: 
        if i not in hexNumbers:
            return None

    decimal = 0
    exponent = 0
    
    for i in num[::-1]:  # Iterate through the characters in reverse order
        decimal += hexNumbers[i] * (16**exponent)
        exponent += 1
    
    return decimal 

# Test cases
print(hex_function("A6F"))
print(hex_function("ZZ"))
print(hex_function("3C000"))

