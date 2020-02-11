def staircase(n):
    space = " "
    hashtag = "#"
    for i in range(1, n+1):
        print(space*(n-i)+hashtag*i)
        