def findAllParents(node, orbitMap, parents):
    """
    Recursively find all parents of a given node, back to the root.

    Inputs: node(str), orbitMap(dict), parents(list)

    Returns: list
    """
    parent = None
    for p in orbitMap:
        # Check if node has parent
        if(node in orbitMap[p]):
            parent = p
            parents.append(p)
            break
    # Find parent of parent found above
    if(parent):
        return findAllParents(node=parent, orbitMap=orbitMap, parents=parents)
    else:
        return parents


if __name__ == "__main__":
    # Read input
    with open("input.txt", "r") as f:
        orbits = f.read().strip().split("\n")
    # Generate parent/child relationships
    orbitMap, keys, values = {}, set(), set()
    for o in orbits:
        o1, o2 = o.split(")")
        if(not orbitMap.get(o1)):
            orbitMap[o1] = []
        orbitMap[o1].append(o2)
        keys.add(o1)
        values.add(o2)
    # Find list of leaf nodes in the tree
    orbitsSet = set()
    leaves = values.difference(keys)
    # Part 1 - Count direct/indirect orbits
    for leaf in leaves:
        parents = findAllParents(node=leaf, orbitMap=orbitMap, parents=[])
        # Loop through pairs in branch
        branch = [leaf] + parents
        for i in range(0, len(branch)):
            for j in range(i+1, len(branch)):
                orbitsSet.add((branch[i], branch[j]))
    print(f"Part 1 - Direct/Indirect Orbits")
    print(f"  Count: {len(orbitsSet)}")
    # Part 2 - Distance from YOU to SAN
    youParents = findAllParents(node="YOU", orbitMap=orbitMap, parents=[])
    sanParents = findAllParents(node="SAN", orbitMap=orbitMap, parents=[])
    # Find common ancestor between YOU and SAN
    distance = 0
    for p in youParents:
        if(p in sanParents):
            distance = youParents.index(p) + sanParents.index(p)
            break
    print(f"Part 2 - Distance from YOU to SAN")
    print(f"  Distance: {distance}")