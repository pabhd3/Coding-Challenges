def createInstruction(instr):
    """
    Generate 5 digit opcode and parameter modes from instruction.

    Input: instr(int)

    Returns: list(int)
    """
    code = str(instr)
    while(len(code) < 5):
        code = f"0{code}"
    return [int(c) for c in code]


def readInstructions(inp, instructions):
    """
    Read a set of instructions passed in, and perform them, adjusting
    the instructions

    Input: pos1(int), pos2(int), instructions(list(int))

    Returns: list(int)
    """
    # Make a copy of instructions to change
    cpy = [i for i in instructions]
    i = 0
    while(True):
        # Get opcode and parameter modes
        _, b, c, d, e  = createInstruction(instr=cpy[i])
        opcode = int(f"{d}{e}")
        if(opcode == 99):
            break
        elif(opcode == 1 or opcode == 2):
            # Get Positions and Values
            p1, p2, p3 = cpy[i+1], cpy[i+2], cpy[i+3]
            v1 = p1 if c==1 else cpy[p1]
            v2 = p2 if b==1 else cpy[p2]
            # Update instructions
            cpy[p3] = v1+v2 if opcode==1 else v1*v2
            i += 4
        elif(opcode == 3):
            # Get position and update instructions
            p1 = cpy[i+1]
            cpy[p1] = inp
            i += 2
        elif(opcode == 4):
            # Get position and update instructions
            p1 = cpy[i+1]
            v1 = p1 if c==1 else cpy[p1]
            print(v1)
            i += 2
        elif(opcode == 5):
            # Get position and update instructions
            p1, p2 = cpy[i+1], cpy[i+2]
            v1 = p1 if c==1 else cpy[p1]
            v2 = p2 if b==1 else cpy[p2]
            i = v2 if v1 else i+3
        elif(opcode == 6):
            # Get position and update instructions
            p1, p2 = cpy[i+1], cpy[i+2]
            v1 = p1 if c==1 else cpy[p1]
            v2 = p2 if b==1 else cpy[p2]
            i = v2 if not v1 else i+3
        elif(opcode == 7):
            # Get position and update instructions
            p1, p2, p3 = cpy[i+1], cpy[i+2], cpy[i+3]
            v1 = p1 if c==1 else cpy[p1]
            v2 = p2 if b==1 else cpy[p2]
            cpy[p3] = 1 if v1 < v2 else 0
            i += 4
        elif(opcode == 8):
            # Get position and update instructions
            p1, p2, p3 = cpy[i+1], cpy[i+2], cpy[i+3]
            v1 = p1 if c==1 else cpy[p1]
            v2 = p2 if b==1 else cpy[p2]
            cpy[p3] = 1 if v1 == v2 else 0
            i += 4


if __name__ == "__main__":
    # Get input & load modules
    with open("input.txt", "r") as f:
        data = f.read()
    instructions = [int(m) for m in data.split(",")]
    # Part 1 - Read Instructions
    print(f"Part 1: Read Instructions")
    readInstructions(inp=1, instructions=instructions)
    # Part 2 - Add opcodes 5-8
    print(f"Part 1: Add Opcodes 5-8")
    readInstructions(inp=5, instructions=instructions)
