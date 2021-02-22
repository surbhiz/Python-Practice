input = [0, 1, 0, 3, 12]
pos = 0
for i in range(len(input)):
    nums = input[i]
    if nums != 0:
        input[pos], input[i] = input[i], input[pos]
        pos += 1


print(input)
