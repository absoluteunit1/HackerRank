def breaking_the_records(scores):
    lowest = highest = scores[0]
    high = low = 0
    for i in scores[1:]:
        if i > highest:
            highest = i 
            high += 1
        elif i < lowest:
            lowest = i
            low += 1
    return f"{high}{low}"
