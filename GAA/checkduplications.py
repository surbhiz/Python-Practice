str = "abcderf"
result = ""
for i in str:
    if i not in result:
        result += i

if str == result:
    print("String is unique")
else:
    print("String is duplicate")
