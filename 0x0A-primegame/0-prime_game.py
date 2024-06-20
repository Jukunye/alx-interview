def play_game(n):
    """
    Use the Sieve of Eratosthenes to find all primes up to n
    and simulate the game.
    """
    # Sieve of Eratosthenes to find all primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Array to store the number of moves needed to reach each number
    moves = [0] * (n + 1)

    # Simulate the game
    for i in range(2, n + 1):
        if is_prime[i]:
            for multiple in range(i, n + 1, i):
                moves[multiple] = moves[i - 1] + 1

    return moves


def isWinner(x, nums):
    """
    This function determines the winner of a prime game played x rounds,
    given an array of starting integers (nums) for each round.

    Args:
        x: Number of rounds played.
        nums: An array of integers (starting from 1) for each round.

    Returns:
        A string indicating the winner ("Maria" or "Ben") or None if
        the winner cannot be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    moves = play_game(max(nums))

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if moves[num] % 2 == 1:  # If the number of moves is odd, Maria wins
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
