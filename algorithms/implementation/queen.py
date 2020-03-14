# n = chessboard size
# r_q, c_q = row and column positions of the queen
# k = number of obstacles
# obtacles = a two dimensional array, which contains tuples that give the x position 
#and the y position of each obstacle
# Output: print (return) the number of squares the queen can attack from her given position 

def queensAttack(n, k, r_q, c_q, obstacles):
    numberOfMoves = 0
    row = r_q
    col = c_q
    
    # for now only works if there are no obtacles. 

    # horizontal and vertical moves available

    numberOfMoves += ((n-1)*2)
    
    # moving down-right
    while( row != 1 and col != n ):
        numberOfMoves += 1
        row -= 1
        col += 1

    row = r_q
    col = c_q

    # moving up-right
    while(row != n and col != n):
        numberOfMoves += 1
        row += 1
        col += 1
    
    row = r_q
    col = c_q

    # moving up-left
    while(row != n and col != 1):
        numberOfMoves += 1
        row += 1
        col -= 1
    
    row = r_q
    col = c_q

    # moving down-left
    while(row != 1 and col != 1):
        numberOfMoves += 1
        row -= 1
        col -= 1
    
    row = r_q
    col = c_q

    return numberOfMoves

# Expect 9
print(queensAttack(4, None, 4, 4, None))

# Expect 14
print(queensAttack(5, None, 4, 4, None))

