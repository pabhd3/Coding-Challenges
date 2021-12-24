def largerDepths(depths):
    """
    Calculate number of depths greater than previous

    Inputs: depths=list(int)

    Returns: int

    Ex. entries=[ 0, 1, 2, 1, 0 ]
        return 3
    """
    # Track previous depth + larger
    prev = None
    larger = 0
    for i, dep in enumerate(depths):
        # Handle 0-index
        if(i == 0):
            prev = dep
        else:
            if(dep > prev):
                larger += 1
            prev = dep
    return larger


def slidingWindow(depths):
    """
    Calculate number of 3-window depths greater than previous

    Inputs: depths=list(int)

    Returns: int

    Ex. entries=[ 0, 1, 2, 3, 2, 1, 0 ]
            --->[ (0,1,2), (1,2,3), (2,3,2), (3,2,1), (2,1,0) ]
            --->[ 3, 6, 7, 6, 3 ]
        return 2
    """
    # Generate 3-tuple windows
    windows = []
    for i, dep in enumerate(depths):
        try:
            windows.append(sum([depths[i], depths[i+1], depths[i+2]]))
        except IndexError:
            continue
    return largerDepths(windows)


if __name__ == "__main__":
    # Load Input
    with open("input.txt", "r") as rf:
        data = rf.read()
    entries = [int(i) for i in data.split("\n")]
    # Part 1 - Find Larger than Previous Depths
    part1 = largerDepths(entries)
    print(f"Part 1\n Larger Depths: {part1}")
    # Part 2 - Find Larger than Previous Window Depths
    part2 = slidingWindow(entries)
    print(f"Part 2\n Sliding Window: {part2}")