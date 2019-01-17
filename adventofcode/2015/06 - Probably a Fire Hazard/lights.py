if __name__ == "__main__":
    # Get data drom flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Loop through each instruction
    lights = {}
    for i in range(0, 1000):
        for j in range(0, 1000):
            lights[(i, j)] = {"state": "off", "brightness": 0}
    for instruction in data.split("\n"):
        print(instruction)
        # Parse the instructions
        instrSplit = instruction.split()
        do, fromCord, toCord = (instrSplit[1], instrSplit[2], instrSplit[4]) if len(instrSplit) == 5 else (instrSplit[0], instrSplit[1], instrSplit[3])
        # Loop through the coordinatess
        for j in range(int(fromCord.split(",")[0]), int(toCord.split(",")[0]) + 1):
            for i in range(int(fromCord.split(",")[1]), int(toCord.split(",")[1]) + 1):
                # Part 1 - Record is light is turned off or on
                # Part 2 - Record brightness of each light
                if(do == "on"):
                    lights[(i, j)]["state"] = "on"
                    lights[(i, j)]["brightness"] += 1
                elif(do == "off"):
                    lights[(i, j)]["state"] = "off"
                    lights[(i, j)]["brightness"] -= 1 if lights[(i, j)]["brightness"] > 0 else 0
                elif(do == "toggle" and lights[(i, j)]["state"] == "on"):
                    lights[(i, j)]["state"] = "off"
                    lights[(i, j)]["brightness"] += 2
                elif(do == "toggle" and lights[(i, j)]["state"] == "off"):
                    lights[(i, j)]["state"] = "on"
                    lights[(i, j)]["brightness"] += 2
    # Calculate Results
    lightsOn, brightness = 0, 0
    for pair in lights:
        lightsOn += 1 if lights[pair]["state"] == "on" else 0
        brightness += lights[pair]["brightness"]
    # Print Results
    print("Part 1\n  Lights on: {total}".format(total="{:,}".format(lightsOn)))
    print("Part 2\n  Total brightness: {total}".format(total="{:,}".format(brightness)))