#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 10, 20, 30],
              [4, 5, 6, 40, 50, 60],
              [7, 8, 9, 70, 80, 90],
              [4, 5, 6, 40, 50, 60],
              [43, 54, 65, 4, 5, 6],
              [77, 88, 99, 76, 87, 98]]

    rotate_2d_matrix(matrix)
    print(matrix)
