# Calculate the smallest Multiple
def smallestMultiple(n):
    smallestMultiple = 1
    while(True):
        evenMultiple = True
        for i in range(1, int(n) + 1):
            if(smallestMultiple % i != 0):
                evenMultiple = False
                break
        if(evenMultiple):
            return smallestMultiple
        smallestMultiple += 1

if __name__ == "__main__":
    # Get user input
    n = input("Enter an integer n: ")
    print("Smallest positive number that is evenly divisible by all of the numbers from 1 to", n)
    # Print results
    print("{:,}".format(smallestMultiple(n)))