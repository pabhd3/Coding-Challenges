from json import load

def findNumbers(obj, intSum, isRed, objSum):
    if(isinstance(obj, dict)):
        # print("Its a dict")
        # print(obj)
        for key in obj:
            if(obj[key] == "red" and isRed == False):
                # print("Object is no good")
                isRed = True
            # print("Key: {}".format(key))
            intSum, isRed, objSum = findNumbers(obj=obj[key], intSum=intSum, isRed=isRed, objSum=objSum)
    elif(isinstance(obj, list)):
        # print("Its a list")
        for item in obj:
            intSum, isRed, objSum = findNumbers(obj=item, intSum=intSum, isRed=isRed, objSum=objSum)
    elif(isinstance(obj, int)):
        # print("Its an int")
        intSum += obj
        # print("Sum is now {}".format(intSum))
    return intSum, isRed, objSum

if __name__ == "__main__":
    # Read the input data
    with open("input.json", "r") as f:
        data = load(f)
        f.close()
    # intSum = findNumbers(obj=data, intSum=0, isRed=False, objSum=0)
    intSum, notRedSum = 0, 0
    for key in data:
        results = findNumbers(obj=data[key], intSum=0, isRed=False, objSum=0)
        print(results)
        intSum += results[0]
        notRedSum += results[0] if not results[1] else 0
    # print("\nSum of all numbers: {}".format(intSum))
    print(intSum, notRedSum)