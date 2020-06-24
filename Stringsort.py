
def sortString(str):
    a_str = input("Enter the string you want to sort:")
    sorted_string = a_str.split()
    sorted_string = [w.lower() + w for w in sorted_string]
    sorted_string.sort()
    sorted_string = [w[len(w)//2:] for w in sorted_string]
    return " ".join(sorted_string)


print(sortString(str))
