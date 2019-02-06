from sys import argv


# Non-functional Calculation
def multiplesOf3or5(n):
    sum = 0
    for i in range(0, int(n)):
        if(i % 3 == 0 or i % 5 ==0):
            sum += i
    return sum


# Functional Calculation
def multiplesOf3or5Functional(n):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(0, int(n))))


# Main
if __name__ == "__main__":
    try:
        print(f"\nSum of multiples of 3 or 5 below {argv[1]}")
        print(f"Non-functional: {multiplesOf3or5(argv[1])}")
        print(f"Functional: {multiplesOf3or5Functional(argv[1])}\n")
    except Exception as error:
        print(f"Error occured: {error}")