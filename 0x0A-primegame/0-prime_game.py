#!/usr/bin/python3
"""prime game module"""


def is_prime(num):
    """generates primes"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """returns winner"""

    if not nums or x < 1 or len(nums) != x:
        return None

    ben = 0
    maria = 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
