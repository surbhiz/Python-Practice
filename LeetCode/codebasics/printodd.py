odd_max = input("Enter the maximum number of your choice")
odd_max = int(odd_max)
odd_numbers = []
for i in range(1, odd_max+1):
    if i % 2 == 1:
        odd_numbers.append(i)
print(odd_numbers)
