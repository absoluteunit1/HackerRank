def birthday(s, d, m):
    ways = 0
    for i in range(0, len(s)):
        sm = 0 
        if len(s) - i >= m:
            for j in range(i, i+m):
                sm += s[j]
            if sm == d:
                ways += 1
    return ways

