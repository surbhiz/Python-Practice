arr = [1, 1, 0, -1, -1]
n = len(arr)
pos = 0
neg = 0
zero = 0
for i in arr:
    if i > 0:
        pos += 1
        prop1 = pos/n
    elif i < 0:
        neg += 1
        prop2 = neg/n
    else:
        zero += 1
        prop3 = zero/n
print("%.6f" % prop1)
print("%.6f" % prop2)
print("%.6f" % prop3)
