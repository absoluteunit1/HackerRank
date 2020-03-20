# My solution

def breakingRecords(scores):
    minScore = scores[0]
    maxScore = scores[0]
    high = 0
    low = 0
    for i in range(1, len(scores)):

        if scores[i] > maxScore:
            high += 1
            maxScore = scores[i]
            
        elif scores[i] < minScore:
            low += 1   
            minScore = scores[i]
            
    return [high, low]

