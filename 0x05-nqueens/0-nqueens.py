#!/usr/bin/python3
"""This module solves the N queens puzzle challenge
"""

import sys


def main():
    """Main function entry point"""

    if len(sys.argv) != 2:
        print("Total arguments should be 2", file=sys.stderr)
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if n < 4:
        print("N should be at least 4", file=sys.stderr)
        sys.exit(1)
    if not 1 <= n <= 32:
        print("N must be between 1 and 32", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
