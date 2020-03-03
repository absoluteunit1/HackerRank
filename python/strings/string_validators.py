def string_validator(s):
    alphanum, alpha, num, lower, upper = False, False, False, False,False
    for letter in s:
        if letter.isalnum():
            alphanum = True
        if letter.isalpha():
            alpha = True
        if letter.isdigit():
            num = True
        if letter.islower():
            lower = True
        if letter.isupper():
            upper = True
    print(f"{alphanum}\n{alpha}\n{num}\n{lower}\n{upper}")

# Other solutions 

def string_validator1(s):
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
    