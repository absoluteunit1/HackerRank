def counting_valleys(n, s):
    location = [0]
    l = 0
   
    valleys = 0

    for i in s:
        if i == "D":
            l -= 1
            location.append(l)
        else:
            l += 1
            location.append(l)

    i = 0
    while(i != len(location) -1):
        i += 1
        if location[i] < 0:
            while(location[i] < 0):
                i += 1
            valleys += 1
        
    return valleys

