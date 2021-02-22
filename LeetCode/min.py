# Python3 implementation to find the
# minimum number of operations in
# which the array A can be converted
# to another array B

# Function to find the minimum
# number of operations in which
# array A can be converted to array B
def checkArray(a, b, n):

    operations = 0
    i = 0

    while(i < n):
        if (a[i]-b[i] == 0):
            i += 1
            continue

        diff = a[i]-b[i]
        i += 1

        while(i < n and a[i]-b[i] == diff):
            i += 1

        operations += 1

    print(operations)


a = [1, 1, 3]
b = [1, 1, 2]
size = len(a)
checkArray(a, b, size)
