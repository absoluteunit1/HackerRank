def camelcase(s):
    return len([i for i in range(len(s)) if s[i].isupper()]) + 1
