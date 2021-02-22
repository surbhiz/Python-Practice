

def is_palindrome_permutation(s: str) -> bool:
    """Given a string, check if it is a permutation of a palindrome."""
    s = s.replace(' ', '').lower()
    left = set()
    for c in s:
        if c in left:
            breakpoint()
            left.remove(c)
        else:
            left.add(c)
    return len(left) < 2


print(is_palindrome_permutation("tact coa"))
