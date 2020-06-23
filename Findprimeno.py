# Python Program to find the prime factors of a number

# Method 1:
def findprimeno(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)

    return factors


num = 630
num1 = 500
print(findprimeno(num))
print(findprimeno(num1))
