if __name__ == "__main__":
    # Get data from flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    niceCountSetA, niceCountSetB = 0, 0
    for name in data.split():
        # Make a list of every two letters
        everyTwoLetters = [name[i] + name[i + 1] for i in range(0, len(name) - 1)]

        # Part 1 - Nice if part 1 rules all met
        # Check if Vowel Count > 2
        vowelCount = True if sum([name.count(vowel) for vowel in ["a", "e", "i", "o", "u"]]) > 2 else False
        # Check if there is repeated letter
        repeatedLetter = True if True in [pair[0] == pair[1] for pair in everyTwoLetters] else False
        # Check if not allowed in name
        notAllowed = True if True not in [sub in name for sub in ["ab", "cd", "pq", "xy"]] else False
        niceCountSetA += 1 if vowelCount and repeatedLetter and notAllowed else 0

        # Part 2 - Nice if part 2 rules all met
        # Check if not shared pair repeat occurs
        repeatPair = False
        # print(name)
        # print(everyTwoLetters)
        for i in range(0, len(everyTwoLetters) - 2):
            # print(everyTwoLetters[i])
            for j in range(i + 2, len(everyTwoLetters)):
                # print(" ", everyTwoLetters[j])
                if(everyTwoLetters[i] == everyTwoLetters[j]):
                    repeatPair = True
                    break
            if(repeatPair):
                break
        # Check if letter repeats with 1 letter between
        repeatSandwich = False
        for i in range(0, len(name) - 2):
            if(name[i] == name[i + 2]):
                repeatSandwich = True
                break
        niceCountSetB += 1 if repeatPair and repeatSandwich else 0
    print("Nice name count under Rule Set 1: {count}".format(count=niceCountSetA))
    print("Nice name count under Rule Set 2: {count}".format(count=niceCountSetB))