import string
# My solution
def minimumNumber(n, password):

    
    numbers = string.digits
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    special_characters = string.punctuation

    pass_length = 0
    result = 0

    nC  = False
    lC  = False
    uC  = False
    sC  = False

    for char in password:
        if char in numbers:
            nC = True
        if char in lower_case:
            lC = True
        if char in upper_case:
            uC = True
        if char in special_characters:
            sC = True
    
    
    if nC == False:
        result += 1
   
    if lC == False:
        result += 1
   
    if uC == False:
        result += 1
    
    if sC == False:
        result += 1
    
    if n < 6:
        pass_length = (6 - n)
    
    return result if result > pass_length else pass_length

# A cleaner solution from the discussion section
# Logic is same as mine but with cleaner code 

def minimumNumber(n, password):
    count = 0    
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1
    return max(count,6-n)