#!/usr/bin/env python
# coding: utf-8

# Write a function that returns a list of all primes up to a given number.
# For each number, in order to determine if it is prime, take the following steps:
# 1. Find the square root of the number
# 2. Find all the primes up to that square root
# 3. Test to see if any of those primes are divisors 
# If a number has no prime divisors, it is prime!

from math import sqrt

def allPrimesUpTo(num):
    
    if num <= 1: 
        return False
    
    square = int(sqrt(num))
    for i in range(2,square+1):
        if num % i == 0:
                return True
                
        else:
            return False
            

print(allPrimesUpTo(1000))
print(allPrimesUpTo(2137))
print(allPrimesUpTo(100))
print(allPrimesUpTo(13))
print(allPrimesUpTo(2000))



