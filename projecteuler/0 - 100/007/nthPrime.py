from math import sqrt, ceil

# Check if a number is prime
def isPrime(n):
    for i in range(2, ceil(sqrt(int(n)))):
        if(int(n) % i == 0):
            return False
    return True
# Find the nth prime number
def nthPrime(n):
    i = 2; count = 0
    while(True):
        if(isPrime(i)):
            count += 1
            if(count == int(n)):
                return i
        i += 1

if __name__ == "__main__":
    # Get user input
    n = input("Enter an integer n: ")
    # Print results
    print("The " + "{:,}".format(int(n)) + "-th prime is")
    print("{:,}".format(nthPrime(n)))