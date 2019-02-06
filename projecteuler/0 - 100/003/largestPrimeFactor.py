from math import sqrt, ceil

# Check if a number is prime
def isPrime(n):
    for i in range(2, ceil(sqrt(n))):
        if(int(n) % i == 0):
            return False
    return True
# Find the largest prime number below n
def largestPrime(n):
    largestPrime = 1
    for i in range(1, int(n)):
        if(isPrime(i) and i > largestPrime and n % i == 0):
            largestPrime = i
    return largestPrime

if __name__ == "__main__":
    # Get user input
    n = input("Enter an integer n: ")
    # Print results
    print("\nLargest Prime below {:,}".format(int(n)))
    print("{:,}".format(largestPrime(n)))