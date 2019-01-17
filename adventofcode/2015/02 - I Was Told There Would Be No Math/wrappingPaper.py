if __name__ == "__main__":
    # Load contents of flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Loop through the presents
    wrappingPaper, ribbon = 0, 0
    for present in data.split():
        # Get the presents dimensions
        dimensions = present.split("x")
        w, l, h = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
        # Part 1 - Find total wrapping paper needed
        wrappingPaper += 2*l*w+ 2*w*h + 2*h*l + min([l*w, w*h, h*l])
        # Part 2 - Find total ribon needed
        ribbon += w*l*h + min([2*(w+l), 2*(w+h), 2*(l+h)])
    # Print Results
    print("Part 1\n  Total square feet needed: {total}".format(total="{:,}".format(wrappingPaper)))
    print("Part 2\n  Total ribbon needed: {total}".format(total="{:,}".format(ribbon)))