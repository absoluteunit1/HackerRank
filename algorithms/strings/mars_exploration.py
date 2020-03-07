def mars_exploration(s):
    expectedMessage = "SOS"*( len(s)//3 )
    return len( [i for i in range(len(s)) if s[i] != expectedMessage[i] ])