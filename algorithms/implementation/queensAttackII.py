# Could not get my solution to pass all tests.
# My original solution used many while loops and as a result was not efficient and would take a long time to run
# This solution is based on the solution in the discussion sections

def queensAttack(n, k, r_q, c_q, obstacles):

    up = n - r_q
    down = r_q - 1
    right = n - c_q
    left = c_q - 1

    rightUp = min(up, right)
    rightDown = min(right,down)
    leftUP = min(left,up)
    leftDown = min(left,down)

    # iterate through each obstacle in the obstacles list of tuples
    for obstacle in obstacles:

        # checks if the obstacle is in the same column as the queen
        if obstacle[1] == c_q:

            # this if/else block checks to see if the obstacle is below the queen or above. Gives the minimum number of moves to the end of board or to the next obstacle. 
            if obstacle[0] < r_q:
                down = min(down, r_q-1-obstacle[0])

            else:
                up = min(up, obstacle[0]-r_q-1)

        # checks if the obstacle is in the same row as the queen
        elif obstacle[0] == r_q:

            # this if/else block checks to see if the obstacle is left or right of the queen. Gives the minimum numbers of moves; either to end of board or to next obstacle in the row
            if obstacle[1] < c_q: 
                left = min(left, c_q-1-obstacle[1])

            else: 
                right = min(right, obstacle[1]-c_q-1)

        # checks if the difference between the obstacle row/queen row and obstacle column/queen column is the same. If so, means that the obstacle is in the same diagonal as the queen
        elif abs(obstacle[0]-r_q) == abs(obstacle[1]-c_q):

            # checks if the obstacle column is right of the queen column (checking to see if the diagonal obstacle is to the right or left of the queen )
            if obstacle[1]>c_q:

                # this if/else block checks if the obstacle row is above or below the queen row (checking to see if the diagonal is right up or right down from the queen).  Takes the minimum of either: the diagonal end of board or the number of moves to the column where the obstacle is
                if obstacle[0]>r_q: 
                    rightUp = min(rightUp, obstacle[1]-c_q-1)

                else: 
                    rightDown = min(rightDown, obstacle[1]-c_q-1)

            # this else block accounts for the obstacle being to the left of the queen column.
            else:

                # this if/else block accounts for the obstacle being up or down from the queen. Takes the minimum of either: the diagonal end of board or the number of moves to the column where the obstacle is
                if obstacle[0]>r_q: 
                    leftUP = min(leftUP, c_q-1-obstacle[1])

                else: 
                    leftDown = min(leftDown, c_q-1-obstacle[1])
    
    # returns the total of all the moves
    
    return up + down + right + left + rightUp + rightDown + leftUP + leftDown