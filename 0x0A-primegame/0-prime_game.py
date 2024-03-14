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


def prime_game(n):
    """calculates wins in prime game"""
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """returns winner of prime game"""
    if not nums or x < 1 or len(nums) != x:
        return None

    winners = [prime_game(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
