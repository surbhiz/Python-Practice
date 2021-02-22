def arePermutation(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    # If length of both strings is not same,
    # then they cannot be Permutation
    if (n1 != n2):
        return False

    # Sort both strings
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)

    # Compare sorted strings
    for i in range(n1):
        if (str1[i] != str2[i]):
            return False

    return True


str1 = "test"
str2 = "ttew"
if (arePermutation(str1, str2)):
    print("Yes")
else:
    print("No")
