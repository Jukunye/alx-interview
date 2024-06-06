#!/usr/bin/python3

def makeChange(coins, total):

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
