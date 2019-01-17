if __name__ == "__main__":
    # Load from flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Movement Directions
    directions = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}
    # Dict to store which houses recieve how many presents
    houses = {(0, 0): 1}
    yearTwoHouses = {(0, 0): 2}
    # Loop through directions
    position = (0, 0)
    santaPosition = (0, 0)
    roboPosition = (0, 0)
    turn = "Santa"
    for direction in data:
        # Part 1 - Mark houses that recieve a present
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        if(not houses.get(position)):
            houses[position] = 1
        else:
            houses[position] += 1
        # Part 2 - Santa and Robo Santa are now sharing present delivery
        if(turn == "Santa"):
            # Directions were sent to Santa
            santaPosition = (santaPosition[0] + directions[direction][0], santaPosition[1] + directions[direction][1])
            if(not yearTwoHouses.get(santaPosition)):
                yearTwoHouses[santaPosition] = 1
            else:
                yearTwoHouses[santaPosition] += 1
            turn = "Robo Santa"
        else:
            # Directions were sent to Robo Santa
            roboPosition = (roboPosition[0] + directions[direction][0], roboPosition[1] + directions[direction][1])
            if(not yearTwoHouses.get(roboPosition)):
                yearTwoHouses[roboPosition] = 1
            else:
                yearTwoHouses[roboPosition] += 1
            turn = "Santa"
    # Print results
    print("Part 1\n  Houses that recieved at least 1 present: {count}".format(count="{:,}".format(len(houses))))
    print("Part 2\n  Year Two Houses that recieved at least 1 present: {count}".format(count="{:,}".format(len(yearTwoHouses))))