def superReducedString(s):
    s = list(s)
    i = 0
    # since we are comparing s[i] and s[i+1], the while loop cannot iterate past the second last item in the list otherwise we will get an Index Error because "last item + 1" index is out of range
    while (i < len(s) - 1) and s != []:
        if s[i] == s[i+1]:
            del s[i] # deletes the list item at the specified index
            del s[i]
            i = 0 # if items are deleted, their index changes so we have to re-start the iteration
        else:
            i += 1 # if nothing is deleted, continue 
    return "".join(map(str,s)) if s != [] else "Empty String" # converts the list to a string and returns the string if its not empty, otherwise returns "Empty String"
    

