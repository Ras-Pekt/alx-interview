#!/usr/bin/python3
"""
Task: 0. Log Parsing
File: 0x06-log_parsing/0-stats.py
"""
from sys import stdin


def print_statistics(total_size, status_codes):
    """prints statistics from the beginning"""
    print("File size: " + str(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {str(status_codes[code])}")


counter = 0
total_size = 0
status_code = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in stdin:
        counter += 1
        line = line.split()

        if len(line) > 1:
            total_size += int(line[-1])

        if len(line) > 2 and line[-2].isnumeric():
            status_code = line[-2]
        else:
            status_code = 0

        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        if counter % 10 == 0:
            print_statistics(total_size, status_codes)

    print_statistics(total_size, status_codes)

except (KeyboardInterrupt):
    print_statistics(total_size, status_codes)
    raise