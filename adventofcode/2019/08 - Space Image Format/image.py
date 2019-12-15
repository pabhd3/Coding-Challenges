if __name__ == "__main__":
    # Get Input Data
    with open("input.txt", "r") as f:
        data = f.read()
    # Set image height/width
    h, w = 6, 25
    # Split input in layers of h*w pixels
    layers = [data[i:i+(h*w)] for i in range(0, len(data), (h*w))]
    # Part 1 - Find layer with fewest 0s
    layerCounts =[(l.count("0"), l.count("1"), l.count("2"))
                for l in layers]
    fewestZeros = sorted(layerCounts, key=lambda x: x[0])[0]
    part1 = fewestZeros[1] * fewestZeros[2]
    print(f"Part 1 - Find layer with fewest 0s")
    print(f"  Number of 1s * 2s: {part1}")
    # Part 2 - Find image
    finalImage = []
    for i in range(0, h*w):
        layerDeep = "".join([l[i] for l in layers])
        for j in layerDeep:
            # Skip transparent (2) pixels
            if(j == "0" or j == "1"):
                finalImage.append(j)
                break
    finalImage = "".join(finalImage).replace("0", " ")
    finalImage = "\n".join([finalImage[i:i+w]
                            for i in range(0, len(finalImage), w)])
    print(f"Part 2 - Find Final Image\n")
    print(finalImage)