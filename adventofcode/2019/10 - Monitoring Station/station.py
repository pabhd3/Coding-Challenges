from fractions import Fraction

with open("input.txt", "r") as f:
    data = f.read().split("\n")

for r in data:
    print(repr(r))

asteroids = []
for x in range(0, len(data)):
    for y in range(0, len(data[0])):
        if(data[x][y] == "#"):
            asteroids.append((x, y))

best, most = None, 0

for a1 in asteroids:
    canSee = set()
    x1, y1 = a1
    for a2 in asteroids:
        if(a1 == a2):
            continue
        x2, y2 = a2
        if(x2 - x1 == 0):
            slope = "0p" if y2>y1 else "0n"
        elif(y2 - y1 == 0):
            slope = "infp" if x2>x1 else "infn"
        else:
            s = Fraction(y2-y1, x2-x1)
            if(x2 > x1):
                q = "q1" if y2 > y1 else "q4"
            else:
                q = "q2" if y2 > y1 else "q3"
            slope = f"{ s }{ q }"
        canSee.add(slope)
    if(len(canSee) > most):
        best, most = a1, len(canSee)

print(best, most)