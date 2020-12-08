# Pip Imports
from re import findall


def checkPolicies1(policies):
    """
    Count passwords that match given policy of count matching

    Input: policies=list(str)

    Ex. policies=['1-2 a: ab', '3-4 b: ab']
        return 1
    """
    valid = 0
    for policy in policies:
        # Parse min, max, letter, password from policy
        regex = r"(\d+)-(\d+) (\w): (\w+)"
        m1, m2, ltr, pwd = findall(regex, policy)[0]
        if(pwd.count(ltr) in range(int(m1), int(m2)+1)):
            valid += 1
    return valid


def checkPolicies2(policies):
    """
    Count passwords that match given policy of positions matching

    Input: policies=list(str)

    Ex. policies=['1-2 a: ab', '3-4 b: abcd']
        return 1
    """
    valid = 0
    for policy in policies:
        # Parse i1, i2, letter, password from policy
        regex = r"(\d+)-(\d+) (\w): (\w+)"
        i1, i2, ltr, pwd = findall(regex, policy)[0]
        # Set for "non-zero" index
        i1, i2 = int(i1)-1, int(i2)-1
        # Check for p1 or p2 but not both ( XOR )
        if(bool(pwd[i1] == ltr) ^ bool(pwd[i2] == ltr)):
            valid += 1
    return valid


if __name__ == "__main__":
    # Load Input
    with open("input.txt", "r") as rf:
        data = rf.read()
    policies = data.split("\n")
    # Part 1 - Find Count Valid Policies 1
    valid1 = checkPolicies1(policies=policies)
    print(f"Part 1\n  Valid Policies 1: { valid1 }")
    # Part 2 - Find Count Valid Policies 2
    valid2 = checkPolicies2(policies=policies)
    print(f"Part 2\n  Valid Policies 2: { valid2 }")