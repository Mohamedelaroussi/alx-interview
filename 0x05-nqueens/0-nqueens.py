#!/usr/bin/python3
"""N Queens puzzle challenge"""
from sys import argv


def close(err: str) -> None:
    """Prints an error message from input validation and exits program"""
    print(err)
    exit(1)


def main() -> None:
    """Starting point and aggregator for the program"""
    if len(argv) != 2:
        close('Usage: nqueens N')
    elif not argv[1].isnumeric():
        close('N must be a number')
    elif int(argv[1]) < 4:
        close('N must be at least 4')


if __name__ == '__main__':
    """Tests the code in this module"""
    main()
