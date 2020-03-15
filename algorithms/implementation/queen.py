# n = chessboard size
# r_q, c_q = row and column positions of the queen
# k = number of obstacles
# obtacles = a two dimensional array, which contains tuples that give the x position 
#and the y position of each obstacle
# Output: print (return) the number of squares the queen can attack from her given position 

# My solution: find the distance from the Queens position to each of the objects in each direction and sum the number of moves between the queen and each object

def queensAttack(n, k, r_q, c_q, obstacles):
    totalNumberOfMoves = 0
    row = r_q
    col = c_q

    moves = 0

    movesRight = n - col
    movesLeft = col -1
    movesTop = n - row
    movesBot = row - 1

    movesBotRight =  min(n-col, row - 1) 
    movesBotLeft = min(col-1, row - 1)
    movesTopRight = min(n - col, n - row)
    movesTopLeft = min(col - 1, n - row)
    
    for obstacle in obstacles:    

        # checking for moves right of the queens position      
                                                                                    
        if obstacle[0] == row and obstacle[1] > col:         
            if (obstacle[1] - col - 1) < movesRight:                 
                movesRight = obstacle[1] - col - 1

        # checking for moves left of the queen's position

        if obstacle[0] == row and obstacle[1] < col:
            if (col - obstacle[1] - 1) < movesLeft:
                movesLeft = col - obstacle[1] -1 
               
        # checking for moves top of the queens position 

        if obstacle[1] == col and obstacle[0] > row:
            if (obstacle[0] - row - 1) < movesTop:      # checking if there are multiple objects in one direction and taking the moves to the closest one
                movesTop = obstacle[0] - row - 1

        # checking for moves below the queens position 

        if obstacle[1] == col and obstacle[0] < row:
            if (row - obstacle[0] - 1) < movesBot:      # checking if there are multiple objects in one direction and taking the moves to the closest one
                movesBot = row - obstacle[0] - 1

        # DIAGONALLY

        # bottom - right

        while( ( row != 1 and col != n ) and (row - 1 != obstacle[0]  and col + 1 != obstacle[1] )):
            col += 1
            row -= 1
            moves += 1    
        if moves < movesBotRight:
            movesBotRight = moves
        moves = 0

        # bottom - left 

        while( ( row != 1 and col != 1 ) and (row - 1 != obstacle[0]  and col - 1 != obstacle[1] )):
            col -= 1
            row -= 1
            moves += 1    
        if moves < movesBotLeft:
            movesBotLeft = moves
        moves = 0

        # top - right

        while( ( row != n and col != n ) and (row + 1 != obstacle[0]  and col + 1 != obstacle[1]  )):
            col += 1
            row += 1
            moves += 1    
        if moves < movesTopRight:
            movesTopRight = moves
        moves = 0

        # top - left

        while( ( row != n and col != 1 ) and (row + 1 != obstacle[0]   and col - 1 != obstacle[1] )):
            col -= 1
            row += 1
            moves += 1    
        if moves < movesTopLeft:
            movesTopLeft = moves
        moves = 0
    
    totalNumberOfMoves = movesBot + movesBotLeft + movesBotRight + movesLeft + movesTopLeft + movesTop + movesTopRight + movesRight
    
    return totalNumberOfMoves

print(queensAttack(5, 3, 4, 3, [(5,5), (4,2), (2,3)] ))