# function to check string is
# palindrome or not
import re


def ispalindrome(str):
    str = input("Enter your string:")
    forwards = ''.join(re.findall(r'[a-z]+', str.lower()))
    backwards = forwards[::-1]
    if(forwards == backwards):
        print("The word,", str, ", is a palindrome ")
    else:
        print("The word,", str, ", is a not palindrome")


print(ispalindrome(str))
