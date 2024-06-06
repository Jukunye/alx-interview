#!/usr/bin/python3
""" This module contains the function makeChanges """


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make the given total.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The target amount to make with the coins.

    Returns:
        int: The minimum number of coins needed to make the total.
             Returns -1 if the total cannot be made
                with the given coin denominations.
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    remaining_amount = total

    # Iterate over each coin in the sorted list
    for coin in coins:
        # Use as many of this coin as possible
        while remaining_amount >= coin:
            coin_count += 1
            remaining_amount -= coin

    # If the total has been reduced to zero, return the number of coins used
    if remaining_amount == 0:
        return coin_count
    # If the total cannot be reduced to zero with the given coins, return -1
    else:
        return -1
