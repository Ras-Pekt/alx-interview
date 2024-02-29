#!/usr/bin/python3
"""
making change module
"""


def makeChange(coins, total):
    """"making change"""
    if total <= 0:
        return 0
    count = 0
    idx = 0
    coins.sort(reverse=True)

    while total > 0 and idx < len(coins):
        largest = coins[idx]
        count += total // largest
        total %= largest
        idx += 1
    if total != 0:
        return -1
    return count
