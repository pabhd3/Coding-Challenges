import itertools, sys, progressbar

# Determine if a number is a palindrome
def isPalindrome(n):
    n = str(n)
    length = len(n)
    for i in range(0, length):
        if(n[i] != n[length-i-1]):
            return False
    return True

# Determine the start and stop points
def startStop(n):
    i = 0; start = 0; stop = 0; foundStart = False
    while(True):
        if(len(str(i)) == int(n) and not foundStart):
            start = i; foundStart = True
        if(len(str(i)) == int(n) + 1):
            stop = i
            return start, stop
        i += 1

# Caclulate the Largest Palindromic Product
def largestPalindromicProduct(n):
    results = startStop(n)
    nDigit = list(range(results[0], results[1]))
    combos = itertools.combinations(nDigit, 2)
    combos2 = itertools.combinations(nDigit, 2)
    length = sum(1 for x in combos2)
    largest = 0; p1 = 0; p2 = 0
    # Display progress checked as a progress bar
    for combo in progressbar.progressbar(combos, max_value=length):
        product = combo[0] * combo[1]
        if(isPalindrome(product) and product > largest):
            largest = product; p1 = combo[0]; p2 = combo[1]
    return largest, p1, p2

if __name__ == "__main__":
    #  Get user input
    n = input("Enter number of digits n: ")
    results = largestPalindromicProduct(n)
    # Print results
    print("Largest Palindromic Product of two " + str(n) + "-digit numbers")
    print(str(results[1]) + " x " + str(results[2]) + " = " + str(results[0]))