l1 = [2, 3, 4, 5]
l2 = [1, 2, 3, 5, 7]
result = []

if len(l1) < len(l2):
    for i in range(0, len(l1)):
        result.append(l1[i]+l2[i])
    print(result)


if len(l1) > len(l2):
    for i in range(0, len(l2)):
        result.append(l1[i]+l2[i])
    print(result)
