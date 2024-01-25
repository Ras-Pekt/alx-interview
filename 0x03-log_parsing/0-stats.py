#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""


if __name__ == "__main__":
    from sys import stdin
    import re

    regex_str = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b - \[.*\] " \
        r"\"\w+\s+/projects/\d+\s+\w+\/1\.1\" \d+ \d+"

    pattern = re.compile(regex_str)
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
            match = pattern.match(line)
            if match:
                counter += 1

                file_size = line.split(" ")[-1]
                status_code = line.split(" ")[-2]
                status_codes[int(status_code)] += 1

                total_size = total_size + int(file_size)
            else:
                continue

            if counter == 10:
                counter = 0
                print(f"File size: {total_size}")

                for code, number in status_codes.items():
                    if number != 0:
                        print(f"{code}: {number}")

    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for code, number in status_codes.items():
            if number != 0:
                print(f"{code}: {number}")
        raise
