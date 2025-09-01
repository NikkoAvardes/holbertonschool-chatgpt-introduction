#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer using recursion.
        The factorial of n (denoted as n!) is the product of all positive integers up to n.
        By definition, 0! = 1.
    
    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)