import json

if __name__ == "__main__":
    # Read data from flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Loop through each instruction
    wires = {}
    for line in data.split("\n"):
        # print(line)
        # Wires involved in instruction
        involvedWires = []
        # Split the instruction and destination wire
        instruction, wire = line.split(" -> ")
        involvedWires.append(wire)
        tempInstruction = instruction
        for operator in ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]:
            tempInstruction = tempInstruction.replace(operator, "")
        tempInstruction = tempInstruction.split()
        # print(tempInstruction)
        try:
            if(int(tempInstruction[1])):
                involvedWires.append(tempInstruction[0])
        except:
            involvedWires.append(tempInstruction[0])
            if(len(tempInstruction) == 2):
                involvedWires.append(tempInstruction[1])
        # Add destination wire if it doesn't already exist
        for involvedWire in involvedWires:
            if(not wires.get(involvedWire)):
                wires[involvedWire] = 0
        # Perform the operation
        if("AND" in instruction):
            a, b = instruction.split(" AND ")[0], instruction.split(" AND ")[1]
            wires[wire] = wires[a] & wires[b]
        elif("OR" in instruction):
            a, b = instruction.split(" OR ")[0], instruction.split(" OR ")[1]
            wires[wire] = wires[a] | wires[b]
        elif("LSHIFT" in instruction):
            a, b = instruction.split(" LSHIFT ")[0], int(instruction.split(" LSHIFT ")[1])
            wires[wire] = wires[a] << b
        elif("RSHIFT" in instruction):
            a, b = instruction.split(" RSHIFT ")[0], int(instruction.split(" RSHIFT ")[1])
            wires[wire] = wires[a] >> b
        elif("NOT" in instruction):
            a = instruction.split("NOT ")[1]
            wires[wire] = ~wires[a]
        else:
            try:
                wires[wire] = int(instruction)
            except:
                wires[wire] = wires[instruction]
    print(json.dumps(wires, indent=2))
    print(wires["a"])