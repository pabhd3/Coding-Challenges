def findPath(directions, intersections=None):
    if(intersections is not None):
        # Relation of known intersections to step count
        path = {i: 0 for i in intersections}
    else:
        # Set of coordinates visited
        path = set()
    x, y, steps = 0, 0, 0
    for d in directions:
        # Pull direction and number of steps
        direct = d[0]
        dist = int(d[1:])
        for _ in range(0, dist):
            steps += 1
            # Update current position
            if(direct == "U"):
                y += 1
            elif(direct == "D"):
                y -= 1
            elif(direct == "L"):
                x -= 1
            else:
                x += 1
            if(not intersections):
                # Mark visited
                path.add((x, y))
            else:
                if((x, y) in path):
                    # Mark number of steps to here
                    path[(x, y)] = steps
    return path


if __name__ == "__main__":
    # Read input
    with open("input.txt", "r") as f:
        data = f.read()
    A, B = data.split("\n")
    A = A.split(",")
    B = B.split(",")
    # Part 1 - Find shortest Manhattan Intersection Distance
    pathA = findPath(directions=A)
    pathB = findPath(directions=B)
    intersections = pathA & pathB
    closest = min([abs(i[0])+abs(i[1]) for i in intersections])
    print(f"Part 1 - Shortest Manhattan Distance to Intersection")
    print(f"  Distance: {closest}")
    # Part 2 - Find shortest distance by steps
    stepsA = findPath(directions=A, intersections=intersections)
    stepsB = findPath(directions=B, intersections=intersections)
    closestSteps = min([abs(stepsA[i])+abs(stepsB[i]) for i in stepsA])
    print(f"Part 2 - Least Steps to Intersection")
    print(f"  Distance: {closestSteps}")