# Solution that passes all test cases from the discussion section 
def repeatedString(s, n):
    # "a" count of full string * number of string repeats + "a" count of last string.
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

