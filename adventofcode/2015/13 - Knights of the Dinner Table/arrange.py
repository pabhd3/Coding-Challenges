from itertools import permutations
from json import dumps


def findHappyness(people):
    print("People:", people)
    total = len(list(permutations(people, len(people))))
    count = 0
    # Loop through seating combinations
    best = {"arrangement": None, "happyness": 0}
    for combo in permutations(people, len(people)):
        happyness = 0
        for i in range(0, len(combo)):
            if(i == 0):
                happyness += happy[combo[i]][combo[i+1]] + happy[combo[i]][combo[len(combo)-1]]
            elif(i == len(combo)-1):
                happyness += happy[combo[i]][combo[0]] + happy[combo[i]][combo[i-1]]
            else:
                happyness += happy[combo[i]][combo[i+1]] + happy[combo[i]][combo[i-1]]
        if(happyness > best["happyness"]):
            best = {"arrangement": combo, "happyness": happyness}
        count += 1
        print("Arrangements Checked: {}/{}".format(count, total), end="\r")
    print("")
    return best


if __name__ == "__main__":
    # Read the instruction data
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Parse the Data
    happy = {}
    for instruction in data.split("\n"):
        # print(instruction.split())
        a, _, net, val, _, _, _, _, _, _, b = instruction.split()
        if(not happy.get(a)):
            happy[a] = {}
        if(not happy[a].get(b)):
            happy[a][b.replace(".", "")] = int(val) if net == "gain" else 0-int(val)
    print("Happyness Values\n{}".format(dumps(happy, indent=4)))
    people = [p for p in happy]
    # Part 1 - Find arrangement with "me"
    print("\nPart 1 - Best Arrangement with 'Me'")
    print(findHappyness(people=people))
    # Part 2 - Find arrangement without "me"
    print("\nPart 2 - Best Arrangement without 'Me'")
    people.remove("Me")
    print(findHappyness(people=people))