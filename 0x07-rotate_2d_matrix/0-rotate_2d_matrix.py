#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates an nxn matrix
    90 degrees clockwise
    """
    m_len = len(matrix)
    m_counter = m_len - 1
    m_list = 0

    rotated_matrix = []

    while m_counter >= 0 and m_list < m_len:
        count = m_len - 1
        # temp_list = []
        # for i in range(len(matrix)):
        #     temp_list.append(matrix[count - i][m_list])
        temp_list = [matrix[count - i][m_list] for i in range(m_len)]
        rotated_matrix.append(temp_list)
        m_counter -= 1
        m_list += 1

    # for i in range(m_len):
    #     for j in range(m_len):
    #         matrix[i][j] = rotated_matrix[i][j]
    matrix[:] = [
        [rotated_matrix[i][j] for j in range(m_len)] for i in range(m_len)
    ]
