s = "2143658709"
result = ''.join([s[i+1] + s[i] for i in range(0, len(s), 2)])
print(result)
