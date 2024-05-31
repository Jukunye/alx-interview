#!/usr/bin/python3
"""This module contains the rotate_2d_matrix function
"""


def rotate_2d_matrix(matrix):
    """Rotates 2D matrix by 90 degrees clockwise
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
