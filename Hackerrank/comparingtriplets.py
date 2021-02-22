def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    i = 0
    j = 0
    while i < len(a) and j < len(b):

        if a[i] > b[j]:
            a_score += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            b_score += 1
            i += 1
            j += 1
        else:
            i += 1
            j += 1

    return a_score, b_score


print(compareTriplets([17, 28, 30], [99, 16, 8]))
