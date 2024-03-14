#!/usr/bin/python3

def generate_primes(n):
    """
    generates primes
    """
    primes = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def isWinner(x, nums):
    """
    returns the winner of the prime game
    """
    if not nums or x < 1 or len(nums) != x:
        return None

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        primes = generate_primes(n)
        while primes:
            if len(primes) % 2 == 0:
                primes.remove(min(primes))
                wins['Maria'] += 1
            else:
                primes.remove(min(primes))
                wins['Ben'] += 1
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
