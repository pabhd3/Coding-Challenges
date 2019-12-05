from random import randint
from numpy import prod

# Calculate the largest product in a series
def largestProductInASeries(choice, n, length):
    default = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843"\
        "8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557"\
        "6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749"\
        "3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776"\
        "6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397"\
        "5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474"\
        "8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586"\
        "1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408"\
        "0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606"\
        "0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    series = default if choice == 'y' else "".join([str(randint(0, 10)) for i in range(0, length)])
    largest = 0
    for i in range(0, length + 1 - n):
        multiples = [series[j] for j in range(i, i + n)]
        product = prod([int(i) for i in multiples])
        if(product > largest):
            largest, largestMultiples = product, multiples
    print("\nSeries")
    index = series.index("".join(largestMultiples))
    print(f"{series[:index]}   {series[index:index+n]}   {series[index+n:]}\n")
    return largest, largestMultiples
# Print the result in a specific format
def printResults(largest, multiples):
    result = f"{largest} = " + " * ".join(multiples)
    print(f"{result}\n")

if __name__ == "__main__":
    # Get user input
    choice = input("Would you like to use the default number? (y/n): ")
    length = 1000
    if(choice == "n"):
        length = input("How many digits do you want to be in the series? ")
    n = input("Enter the number of adjacent digits, n: ")
    largest, multiples = largestProductInASeries(choice, int(n), int(length))
    # Print results
    print("The largest product in the above series of " + n + " adjacent digits")
    printResults(largest, multiples)