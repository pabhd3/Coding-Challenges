# Pip Imports
from itertools import combinations


def product(items):
    """
    Calculate the product of list of numbers

    Input: items=list(int)

    Returns: int

    Ex. items=[ 1, 2, 3, 4 ]
        return 24
    """
    p = 1
    for i in items:
        p *= i
    return p


def findSum(entries, n, total):
    """
    Find the product of n items that sum to total

    Input: entries=list(int), n=int, total=int

    Ex. entries=[ 1, 2, 3 ], n=2, total=5
        return 6
    """
    for c in combinations(entries, n):
        if(sum(c) == total):
            return product(items=c)


if __name__ == "__main__":
    # Load Input
    with open("input.txt", "r") as rf:
        data = rf.read()
    entries = [int(i) for i in data.split("\n")]
    # Part 1 - Sum 2 to 2020
    sum2 = findSum(entries=entries, n=2, total=2020)
    print(f"Part 1\n  2 Multiplied Expense: { sum2 }")
    # Part 2 - Sum 3 to 2020
    sum3 = findSum(entries=entries, n=3, total=2020)
    print(f"Part 2\n  3 Multiplied Expense: { sum3 }")
