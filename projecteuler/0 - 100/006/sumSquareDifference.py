from sys import argv

# Calculate the sum of the squares
def squareSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += pow(i, 2)
    return sum

# Functionally calculate the sum of the squares
def squareSumFunctional(n):
    return sum(map(lambda x: x**2, range(1, n + 1)))

# Calculate the square of the sum
def sumSquares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return pow(sum, 2)

# Functionally calculate the square of the sum
def sumSquaresFunctional(n):
    return pow(sum(range(1, n + 1)), 2)

if __name__ == "__main__":
    try:
        # Get user input
        n = int(argv[1])
        s1, s2 = sumSquares(n), squareSum(n)
        s1Functional, s2Functional = sumSquaresFunctional(n), squareSumFunctional(n)
        # Print results
        print(f"\nDifference between the sum of squares of the first {n} natural numbers and the square of the sum:")
        print(f"\nNon functional: {s2} - {s1} = {s2 - s1}")
        print(f"Functional: {s2Functional} - {s1Functional} = {s2Functional - s1Functional}\n")
    except Exception as error:
        print(f"Error occured: {error}")