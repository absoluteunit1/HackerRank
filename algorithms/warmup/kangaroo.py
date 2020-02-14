def kangaroo(x1, v1, x2, v2):
    count = 1
    possible = "YES"
    while(x1 + v1*count != x2 + v2*(count)):
        count += 1
        if count >= 10000:
            possible = "NO"
            break
    return possible
   

