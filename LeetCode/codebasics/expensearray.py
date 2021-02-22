month = ["January", "February", "March", "April", "May"]
expenses = [2200, 2350, 2600, 2130, 2190]

print(
    f"In {month[1]} you spent {expenses[1]-expenses[0]} extra compare to {month[0]}")

print(f"Total expense in first quarter is ", sum(expenses[0:3]))

print(f"Did you spend exactly $2000 in any month?", 2000 in expenses)
month.append("June")
expenses.append(1980)

expenses[3] = expenses[3]+200
print(expenses)
print(month)
