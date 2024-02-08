#!/usr/bin/python3
"""
a method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    byte_count = 0

    for byte in data:
        mask = 1 << 7
        if not byte_count:
            while byte & mask:
                byte_count += 1
                mask >>= 1
            if not byte_count:
                continue
            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        byte_count -= 1
    return byte_count == 0
