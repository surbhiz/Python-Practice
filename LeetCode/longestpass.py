
def solution(S):
    longest = -1
    num_of_letters = 0
    num_of_digits = 0
    num_of_others = 0
    for letter in S:
        if letter.isalpha():
            num_of_letters += 1
        elif letter.isdigit():
            num_of_digits += 1
        elif letter == " ":
            # Check whether it's a valid password.
            if num_of_others == 0 and \
               num_of_letters % 2 == 0 and \
               num_of_digits % 2 == 1:
                if longest < num_of_letters + num_of_digits:
                    longest = num_of_letters + num_of_digits
            # Reset the counters for the next word.
            num_of_letters = 0
            num_of_digits = 0
            num_of_others = 0
        else:
            num_of_others += 1
    # Check whether the last word is a valid password.
    if num_of_others == 0 and \
       num_of_letters % 2 == 0 and \
       num_of_digits % 2 == 1:
        if longest < num_of_letters + num_of_digits:
            longest = num_of_letters + num_of_digits
    return longest


print(solution("Hellozzz"))
