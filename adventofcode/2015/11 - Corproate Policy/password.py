def increment(password):
    # Convert Chars to Ints
    passwordOrd = [ord(i) for i in password]
    passwordOrd[7] += 1
    # Add 1, and set z -> a
    for i in range(7, -1, -1):
        if(passwordOrd[i] > 122):
            passwordOrd[i] = 97
            try:
                passwordOrd[i-1] += 1
            except:
                pass
    return "".join([chr(i) for i in passwordOrd])


if __name__ == "__main__":
    # Starting Password
    password = "hxbxwxba"
    print("\nStarting Password: {}\n".format(password))
    # Find new password
    newPasswords = []
    found = False
    count = 0
    while(not found):
        password = increment(password=password)
        # Test 1 - Check if one set of sequential exists. abc, efg, hij...
        test1 = False
        for i in range(0, 6):
            a, b, c = ord(password[i]), ord(password[i+1]), ord(password[i+2])
            if(b == a + 1 and c == a + 2):
                test1 = True
                break
        # Test 2 - Cannot contail 'i', 'o', or 'l'
        test2 = False
        if("i" not in password and "o" not in password and "l" not in password):
            test2 = True
        # Test 3 - Contain two different non overlapping pairs
        test3 = False
        pairs = [password[i] + password[i+1] for i in range(0, 7)]
        for i in range(0, 5):
            for j in range(i+2, 7):
                a, b = pairs[i], pairs[j]
                if(a[0] == a[1] and b[0] == b[1] and a[0] != b[0]):
                    test3 = True
        # Break from loop
        if(test1 and test2 and test3):
            newPasswords.append(password)
        found = True if len(newPasswords) == 2 else False
        count += 1
        print("Passwords Checked: {}".format(count), end="\r")
    # Print Results
    print("\n\n1st New Password: {}".format(newPasswords[0]))
    print("\n2nd New Password: {}".format(newPasswords[1]))
