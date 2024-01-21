#!/usr/bin/python3
"""
A function that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0
    a = 2
    b = 0
    while a <= n:
        if n % a == 0:
            b += a
            n = n / a
        else:
            a += 1
    return b
