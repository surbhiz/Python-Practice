def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def Selection_Sort(arr):
    new_Array = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_Array.append(arr.pop(smallest))
    return new_Array


print(Selection_Sort([10, 5, 7, 1, 2]))
