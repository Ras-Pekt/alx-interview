#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
from sys import stdin


def print_statistics():
    """prints statistics from the beginning"""
    print(f'Total file size: {total_size}')
    for code, number in status_codes.items():
        if number != 0:
            print(f'{code}: {number}')


status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

counter = 0
total_size = 0

try:
    for line in stdin:
        line = line.strip()
        counter += 1

        try:
            log_list = line.split()
            status_code = int(log_list[-2])
            file_size = int(log_list[-1])
        except (ValueError):
            continue

        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        if counter % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    raise
