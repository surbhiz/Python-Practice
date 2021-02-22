s = "bbbbb"
result = []
count = 0
for i in range(len(s)-1):
    result.append(s[i])
    for j in range(i+1, len(s)):
        if s[j] not in result:
            result.append(j)
        else:
            if(len(result) > count):
                count = len(result)
            break
    if(len(result) > count):
        count = len(result)
print((count))
