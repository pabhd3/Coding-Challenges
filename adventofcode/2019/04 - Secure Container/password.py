def findPassword(pRange):
    start, end = pRange.split("-")
    possibilities = []
    for p in range(int(start), int(end)+1):
        # Check if 6 digit number
        if(len(str(p)) != 6):
            continue
        # Check for at 1 pair of adjacent same numbers
        double = False
        strP = str(p)
        for i in range(0, 5):
            if(strP[i] == strP[i+1]):
                double = True
                break
        if(not double):
            continue
        #Check for never decreasing
        decrease = False
        for i in range(0, 5):
            if(int(strP[i]) > int(strP[i+1])):
                decrease = True
                break
        if(decrease):
            continue
        possibilities.append(p)
    return possibilities


def noLargerSets(possibilities):
    newPoss = []
    for p in possibilities:
        strP = str(p)
        temp = {}
        for i in strP:
            try:
                temp[i] += 1
            except:
                temp[i] = 1
        if(2 not in [temp[i] for i in temp]):
            continue
        newPoss.append(p)
    return newPoss



if __name__ == "__main__":
    # Read input
    with open("input.txt", "r") as f:
        data = f.read()
    # Part 1 - Find password
    possibilities = findPassword(pRange=data)
    print(f"Part 1 - Find Password Possibilities")
    print(f"  Possiblities: {len(possibilities)}")
    # Part 2 - No Larger Sets
    newPossibilities = noLargerSets(possibilities=possibilities)
    print(f"Part 2 - \"No Larger Sets Rule\" Possibilities")
    print(f"  Possibilties: {len(newPossibilities)}")
