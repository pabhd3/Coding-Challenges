def calculateFuel(mass):
    """
    Calculation used to find fuel requirement based of mass

    Input: mass=int

    Returns: int
    """
    return (mass // 3) - 2


def fuelRequirement(modules):
    """
    Part 1 - Find the sum of all fuel required for modules on your ship

    Input: modules=list(int)

    Returns: int
    """
    return sum([calculateFuel(mass=m) for m in modules])


def recursiveFuelRequirement(modules):
    """
    Part 2 - Find sum of fuel required for modules + fuel for required fuel +
             fuel for required fuel's fuel + etc. on your ship

    Input: modules=list(int)

    Returns: int
    """
    fuel = 0
    for m in modules:
        mass = m
        while(True):
            fNeeded = calculateFuel(mass=mass)
            if(fNeeded < 0):
                break
            fuel += fNeeded
            mass = fNeeded
    return fuel


if __name__ == "__main__":
    # Get input & load modules
    with open("input.txt", "r") as f:
        data = f.read()
    modules = [int(m) for m in data.split("\n")]
    print(f"Modules Found: {len(modules)}\n")
    # Part 1 - Fuel Requirement
    requiredFuel = fuelRequirement(modules=modules)
    print(f"Part 1\n  Fuel Requirement: {requiredFuel}")
    # Part 2 - Recursive Fuel Requirement
    recursiveRequiredFuel = recursiveFuelRequirement(modules=modules)
    print(f"Part 2\n  Recursive Fuel Requirement: {recursiveRequiredFuel}")
