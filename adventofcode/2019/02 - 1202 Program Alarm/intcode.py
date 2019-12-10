def readInstructions(pos1, pos2, instructions):
    """
    Read a set of instructions passed in, and perform them, adjusting
    the instructions

    Input: pos1(int), pos2(int), instructions(list(int))

    Returns: list(int)
    """
    # Make a copy of instructions to change
    cpy = [i for i in instructions]
    cpy[1], cpy[2] = pos1, pos2
    i = 0
    while(i < len(instructions)):
        if(cpy[i] == 99):
            # Break out of instructions
            break
        else:
            # Get Positions and Values
            i1, i2, i3 = i+1, i+2, i+3
            p1, p2, p3 = cpy[i1], cpy[i2], cpy[i3]
            v1, v2 = cpy[p1], cpy[p2]
            # Adjust copy of instructions
            cpy[p3] = v1+v2 if cpy[i]==1 else v1*v2
            i += 4
    return cpy


if __name__ == "__main__":
    # Get input & load modules
    with open("input.txt", "r") as f:
        data = f.read()
    instructions = [int(m) for m in data.split(",")]
    print(f"Instructions Found: {instructions}\n")
    # Part 1 - Read Instructions
    newInstr = readInstructions(pos1=12, pos2=2, instructions=instructions)
    print(f"Part 1: Read Instructions")
    print(f"  Index 0: {newInstr[0]}")
    # Part 2 - Find Noun Verb
    found, noun, verb = False, None, None
    for n in range(0, 101):
        for v in range(0, 101):
            nvInstr = readInstructions(pos1=n, pos2=v,
                                       instructions=instructions)
            if(nvInstr[0] == 19690720):
                found, noun, verb = True, n, v
                break
        if(found):
            break
    print(f"Part 2: Find Noun & Verb")
    print(f"  100 * {noun} + {verb} = {100 * noun + verb}")
