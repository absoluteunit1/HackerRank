# n = money to spend
# c = cost of one cholocate 
# number of wrappers to get a free bar

def chocolateFeast(n, c, m):
    chocolates_bought = n//c
    chocolates_eaten = chocolates_bought
    wrappers_left = chocolates_bought 

    while(wrappers_left >= m):
            chocolates_bought = wrappers_left//m 
            wrappers_left = chocolates_bought + wrappers_left % m
            chocolates_eaten += chocolates_bought
    return chocolates_eaten


