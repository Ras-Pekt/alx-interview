#!/usr/bin/python3
"""alx interview"""


def pascal_triangle(n):
    """prints pascal's triangle"""
    if n <= 0:
        return []

    pascal = [[1]]
    for _ in range(1, n):
        last_row = pascal[-1]
        next_row = [1]
        for i in range(len(last_row) - 1):
            next_row.append(last_row[i] + last_row[i+1])
        next_row.append(1)
        pascal.append(next_row)

    return pascal
