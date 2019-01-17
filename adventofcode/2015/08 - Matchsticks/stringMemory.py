import re, binascii

if __name__ == "__main__":
    # Load the data from flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Loop through each line
    codeCount, memCount, newEncode = 0, 0, 0
    for line in data.split("\n"):
        print("\nOriginal --> {}".format(line))
        # Determine Code Length
        print("  Code Count: {}".format(len(line)))
        codeCount += len(line)
        memLine = line[1:-1]
        # Determine Memory Length
        memLine = memLine.replace("\\\\", "\\")
        memLine = memLine.replace('\\"', '"')
        for h in re.findall(r"\\x([a-f0-9][a-f0-9])", memLine):
            memLine = memLine.replace("\\x{}".format(h), "h")
        print("Memory Code -->", memLine)
        print("  Memory Count: {}".format(len(memLine)))
        memCount += len(memLine)
        # Determine Newly Encoded
        encoded = '"{}"'.format(line.replace('\\', '\\\\').replace('"', '\\"'))
        print("Newly Encoded -->", encoded)
        print("  Encoded Count: {}".format(len(encoded)))
        newEncode += len(encoded)
    print("\nResults")
    print("  Part 1: (Code Count)", codeCount, "- (Memory Count)", memCount, "=", codeCount - memCount)
    print("  Part 2: (Encoded Count)", newEncode, "- (Original Count)", codeCount, "=", newEncode - codeCount)