# Import md5 to find hash values
from hashlib import md5

if __name__ == "__main__":
    # Set Secret Key
    key = "yzbqklnj"
    number = 0
    fiveZeros = {"lowest": 0, "found": False}
    sixZeros = {"lowest": 0, "found": False}
    while(not fiveZeros["found"] or not sixZeros["found"]):
        # Find the MD5 Hash
        result = md5("{key}{number}".format(key=key, number=number).encode())
        hexDigest = result.hexdigest()
        # Part 1 - Check if Hash starts with '00000'
        if(hexDigest.startswith("00000") and not fiveZeros["found"]):
            fiveZeros = {"lowest": number, "found": True}
        # Part 2 - Check if Hash starts with '000000'
        if(hexDigest.startswith("000000") and not sixZeros["found"]):
            sixZeros = {"lowest": number, "found": True}
        number += 1
    # Print Results
    print("Lowest number for five zeros: {lowest}".format(lowest=fiveZeros["lowest"]))
    print("Lowest number for six zeros: {lowest}".format(lowest=sixZeros["lowest"]))