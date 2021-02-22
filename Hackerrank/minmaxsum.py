arr = [7, 69, 2, 221, 8974]
n = len(arr)
arr.sort()
minsum = 0
maxsum = 0

i = 0
while i < n-1:
    minsum += arr[i]
    i += 1
print(minsum)
j = 1
while j < n:
    maxsum += arr[j]
    j += 1
print(maxsum)
