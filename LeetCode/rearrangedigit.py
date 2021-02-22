

def smallestnum(self, N):
    for i, n in enumerate(N):
        if n != '0':
            temp = N.pop(i)
            break
    return str(temp)+''.join(N)


lst = list(str(570107))
lst.sort()
print(smallestnum('', lst))
