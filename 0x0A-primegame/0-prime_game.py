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

    wins = {
        "ben": 0, "maria": 0
    }

    for num in nums:
        primes = [i for i in range(2, num + 1) if is_prime(i)]
        if len(primes) % 2 == 0:
            wins["ben"] += 1
        else:
            wins["maria"] += 1

    if wins["maria"] > wins["ben"]:
        return "Maria"
    elif wins["ben"] > wins["maria"]:
        return "Ben"
    else:
        return None
