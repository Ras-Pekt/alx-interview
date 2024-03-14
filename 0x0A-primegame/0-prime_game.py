#!/usr/bin/python3
"""prime game module"""


# def generate_primes(n):
#     """
#     generates primes
#     """
#     primes = []
#     for i in range(2, n + 1):
#         is_prime = True
#         for j in range(2, i**0.5 + 1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(i)
#     return primes


def isWinner(x, nums):
    """
    Returns the winner
    """
#     if not nums or x < 1 or len(nums) < x:
#         return None

#     wins = {"ben": 0, "maria": 0}
#     i = 0

#     while i < x:
#         primes = generate_primes(nums[i])
#         if len(primes) % 2 == 0:
#             wins["ben"] += 1
#         else:
#             wins["maria"] += 1
#         i += 1

#     if wins["ben"] > wins["maria"]:
#         return 'Ben'
#     elif wins["maria"] > wins["ben"]:
#         return 'Maria'
#     else:
#         return None

    num = max(nums)
    primes = [True for _ in range(max(num + 1, 2))]
    for i in range(2, int(pow(num, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, num + 1, i):
            primes[j] = False

    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c

    winner = ''
    player1 = 0
    for num in nums:
        player1 += primes[num] % 2 == 1
    if player1 * 2 == len(nums):
        winner = None
    if player1 * 2 > len(nums):
        winner = "Maria"
    else:
        winner = "Ben"
    return winner
