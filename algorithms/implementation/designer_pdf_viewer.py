import string

def designer_pef_viewer(h, word):
    length = len(word)
    alphabet = list(string.ascii_lowercase) # create a lower casr list of the alphabets 
    
    # for every letter in the word find the correspoding height by using the index of 
    # the letter in the alphabet as the index in the height list  and take the max of 
    # those heights
   
    height = max([ h[alphabet.index(letter)] for letter in word ]) 
    return height*length
