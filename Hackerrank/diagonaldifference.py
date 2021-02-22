arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
n = len(arr)
sum = 0
i = 0
j = 0
while i < n:
    if arr[i] == arr[j]:
        sum += arr[i][j]
        i += 1
        j += 1
        continue
print(sum)

sum1 = 0
i1 = 0
j1 = n-1
while i1 < n:
    sum1 += arr[i1][j1]
    i1 += 1
    j1 -= 1
    continue
print(sum1)

print(abs(sum-sum1))
