if __name__ == "__main__":
    # Load the input data
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Go up a floor if "(", do down a floor if ")"
    steps = {"(": 1, ")": -1}
    # Part 1 - Find floor we end on
    floor, basement = 0, {"index": 0, "found": False}
    for step in data:
        floor += steps[step]
        # Part 2 - Find index we enter basement at
        if(floor != -1 and basement["found"] == False):
            basement["index"] += 1
        elif(floor == -1 and basement["found"] == False):
            basement["index"] += 1
            basement["found"] = True
    # Print Results
    print("Part 1\n  End on floor: {floor}".format(floor=floor))
    print("Part 2\n  Enter basement as index: {index}".format(index=basement["index"]))