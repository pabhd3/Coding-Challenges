from itertools import permutations
from json import dumps

if __name__ == "__main__":
    # Read data from flatfile
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Create a list of cities to visit
    cities = set()
    distances = {}
    for row in data.split("\n"):
        start, _, end, _, dist = row.split()
        # Record Cities
        cities.add(start)
        cities.add(end)
        # Record distance between cities
        if(not distances.get(start)):
            distances[start] = {}
        distances[start][end] = int(dist)
        if(not distances.get(end)):
            distances[end] = {}
        distances[end][start] = int(dist)
    # Try each combination of cities
    shortest = {"dist": float("inf"), "route": None}
    longest = {"dist": 0, "route": None}
    for route in permutations(cities, len(cities)):
        routeDistance = 0
        for i in range(0, len(route) - 1):
            try:
                a, b = route[i], route[i + 1]
                routeDistance += distances[a][b]
            except:
                routeDistance = None
        # Part 1 - Find Shortest Distance
        if(routeDistance and routeDistance < shortest["dist"]):
            shortest = {"dist": routeDistance, "route": route}
        # Part 2 - Find Longest Distance
        if(routeDistance and routeDistance > longest["dist"]):
            longest = {"dist": routeDistance, "route": route}
    # print(dumps(distances, indent=4))
    print("Shortest Distance", dumps(shortest, indent=2))
    print("Longest Distance", dumps(longest, indent=2))