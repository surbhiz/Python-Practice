def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)


countdown(1)

# using stack in recursion


def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))


print(fact(5))

# using recursion  calculate sum of array


def sum(arr):
    if arr == []:
        return 0
    return arr[0]+sum(arr[1:])


print(sum([1, 2, 5]))

# without recursion calculate sum of array


def sum1(arr):
    total = 0
    if arr == []:
        return 0
    else:
        for i in arr:
            total += i

        return total


print(sum1([1, 2, 5]))

# using recusion count numbers in array


def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


print(count([1, 2, 3, 4]))

# without using recursion count numbers in array


def count1(arr):
    if arr == []:
        return 0
    else:
        for i in range(len(arr)):
            i += 1
        return i


print(count1([0]))


# maximum number in list using recursion

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max([5, 4, 10]))


def multiply(arr):
    for i in range(1, len(arr)):
        return arr[i]*arr


print(multiply([1, 2, 2]))
