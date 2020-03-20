import string
# Solution One: Using sets and comparing them.
# Sets are unordered and set elements are unique (duplicates not allowed)

def pangrams(s):
    setS = set(s.lower().replace(" ", ""))
    alphabet = set(string.ascii_lowercase)
    return "pangram" if setS == alphabet else "not pangram"
