# function to check string is
# palindrome or not
import re


def ispalindrome(str):
    forwards = ''.join(re.findall(r'[a-z]+', str.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


str = input("Enter your string:")
print(ispalindrome(str))
