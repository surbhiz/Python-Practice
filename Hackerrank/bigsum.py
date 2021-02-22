def aVeryBigSum(ar):

    n = len(ar)
    if n > 10:
        return "Invalid Input"
    sum = 0
    i = 0
    while i < n:
        if ar[i] > pow(10, 10):
            return
        else:
            sum += ar[i]
            i += 1
    return sum


print(aVeryBigSum([1000000001, 1000000001,
                   1000000001, 1000000001, 100000000001]))
