# p = price 
# d = dollars lesss than the cost of the previous one
# m = the lowest price possible. 
# return the max number of games that can be bought

# My solution

def howManyGames(p, d, m, s):
    gamesPurchased = 0
    while(s >= 0):
        s -= p
        p = max(p-d, m)
        gamesPurchased += 1
    return gamesPurchased - 1  # we put the -1 here because on the last iteration, we go beyond s and purchase a game, so we have to subtract that game from the number of games purchased
    

