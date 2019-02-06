from sys import argv


# Generate the Fibonacci list, stopping at given value
def generateFibonacci(n):
    fib = [1, 1]
    for i in range(0, int(n)):
        if(fib[i-1] + fib[i-2] > int(n)):
            break
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib


# Calculate even-valued sum
def evenFibonacciNumbers(n):
    sum = 0
    for value in generateFibonacci(n):
        if(value % 2 == 0):
            sum += value
    return sum


# Calculate even-valued sum (functional)
def evenFibonacciNumbersFunctional(n):
    return sum(filter(lambda x: x % 2 == 0, generateFibonacci(n)))


if __name__ == "__main__":
    try:
        print(f"\nSum of even-valued fibonacci terms below: {argv[1]}")
        print(generateFibonacci(argv[1]))
        print(f"\nNon-functional: {evenFibonacciNumbers(argv[1])}")
        print(f"Functional: {evenFibonacciNumbersFunctional(argv[1])}\n")
    except Exception as error:
        print(f"Error occured: {error}")