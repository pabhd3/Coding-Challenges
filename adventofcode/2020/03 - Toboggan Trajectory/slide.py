def product(items):
    """
    Calculate the product of list of numbers

    Input: items=list(int)

    Returns: int

    Ex. items=[ 1, 2, 3, 4 ]
        return 24
    """
    p = 1
    for i in items:
        p *= i
    return p


def parseData(data):
    """
    Parse a grid into a list of "columns"

    Input: data=str

    Ex. data="...\n###\n..."
        return ['.#.', '.#.', '.#.']
    """
    columns = []
    rows = data.split("\n")
    # Loop through each "column"
    for c in range(0, len(rows[0])):
        column = ""
        # Add all each row value by index
        for r in rows:
            column += r[c]
        columns.append(column)
    return columns


def slide(columns, slope):
    # Set up traverse tracking
    x, y, trees = 0, 0, 0
    sx, sy = slope
    numRows = len(columns[0])
    numColumns = len(columns)
    while(y < numRows):
        # Check if we hit a tree
        if(columns[x][y] == "#"):
            trees += 1
        # Update position
        x = (x + sx) % numColumns
        y += sy
    return trees


def multiSlide(columns, slopes):
    # Return product of trees per slope
    return product(items=[slide(columns=columns, slope=slope)
                          for slope in slopes])


if __name__ == "__main__":
    # Load and Parse input
    with open("input.txt", "r") as rf:
        data = rf.read()
    columns = parseData(data=data)
    # Part 1 - Find trees hit
    treesHit = slide(columns=columns, slope=(3, 1))
    print(f"Part 1\n  Trees Hit: { treesHit }")
    # Part 2 - Product of multiple slopes
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    treeProduct = multiSlide(columns=columns, slopes=slopes)
    print(f"Part 2\n  Multi-Slope Product: { treeProduct }")