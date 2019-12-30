from itertools import combinations
from numpy import product


moonPositions = lambda moons, oc: [(moons[m][axis]["p"][oc], moons[m][axis]["v"][oc]) for axis in ("x", "y", "z") for m in mKeys]


def printMoons(moons, space):
    print("\n")
    for m in moons:
        px, py, pz = moons[m]["x"]["p"], moons[m]["y"]["p"], moons[m]["z"]["p"]
        vx, vy, vz = moons[m]["x"]["v"], moons[m]["y"]["v"], moons[m]["z"]["v"]
        print(f"{' '*space}pos=<x={px}, y={py}, z={pz}>, vel=<x={vx}, y={vy}, z={vz}>")
    print("\n")


def moveMoons(moons, keys, combos):
    for mPair in combos:
        m1, m2 = mPair
        for axis in ("x", "y", "z"):
            # Apply Gravity
            if(moons[m1][axis]["p"]["c"] != moons[m2][axis]["p"]["c"]): 
                m1LTm2 = moons[m1][axis]["p"]["c"] < moons[m2][axis]["p"]["c"]
                moons[m1][axis]["v"]["c"] += 1 if m1LTm2 else -1
                moons[m2][axis]["v"]["c"] += -1 if m1LTm2 else 1
    for m in keys:
        for axis in ("x", "y", "z"):
            # Apply Velocity
            moons[m][axis]["p"]["c"] += moons[m][axis]["v"]["c"]


def resetMoons(moons):
    for m in moons.keys():
        for axis in ("x", "y", "z"):
            moons[m][axis]["p"]["c"] = moons[m][axis]["p"]["o"]
            moons[m][axis]["v"]["c"] = moons[m][axis]["v"]["o"]


moons = {
    "Io": {
        "x": { "p": { "o": 5, "c": 5 }, "v": { "o": 0, "c": 0 } },
        "y": { "p": { "o": 4, "c": 4 }, "v": { "o": 0, "c": 0 } },
        "z": { "p": { "o": 4, "c": 4 }, "v": { "o": 0, "c": 0 } }
    },
    "Europa": {
        "x": { "p": { "o": -11, "c": -11 }, "v": { "o": 0, "c": 0 } },
        "y": { "p": { "o": -11, "c": -11 }, "v": { "o": 0, "c": 0 } },
        "z": { "p": { "o": -3, "c": -3 }, "v": { "o": 0, "c": 0 } }
    },
    "Ganymede": {
        "x": { "p": { "o": 0, "c": 0 }, "v": { "o": 0, "c": 0 } },
        "y": { "p": { "o": 7, "c": 7 }, "v": { "o": 0, "c": 0 } },
        "z": { "p": { "o": 0, "c": 0 }, "v": { "o": 0, "c": 0 } }
    },
    "Callisto": {
        "x": { "p": { "o": -13, "c": -13 }, "v": { "o": 0, "c": 0 } },
        "y": { "p": { "o": 2, "c": 2 }, "v": { "o": 0, "c": 0 } },
        "z": { "p": { "o": 10, "c": 10 }, "v": { "o": 0, "c": 0 } }
    }
}

mKeys = moons.keys()
mCombos = list(combinations(moons.keys(), 2))

printMoons(moons=moons, space=0)

for _ in range(0, 1000):
    moveMoons(moons=moons, keys=mKeys, combos=mCombos)

energy = sum([product((
              sum(abs(moons[m][axis]["p"]["c"]) for axis in ("x","y","z")), 
              sum(abs(moons[m][axis]["v"]["c"]) for axis in ("x","y","z"))
              )) for m in mKeys])
print(energy)