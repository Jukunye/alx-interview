#!/usr/bin/python3
"""
This module contains the function minOperations"""


def minOperations(n):
    """
    Calculates fewest number of operations needed to result in a given
    number of desired characters"""

    min_ops = 0

    if n <= 1:
        return 0

    for i in range(2, n + 1):
        while n % i == 0:
            n = n / i
            min_ops += i
    return min_ops
