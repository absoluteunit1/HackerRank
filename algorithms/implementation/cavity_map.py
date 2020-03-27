def cavityMap(n, grid):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i][j] > max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):    # this comparison works because "X">"9">"1". Strings are considered higher than digits ("9") in Python. 
                grid[i] = grid[i][:j] +'X' + grid[i][j+1:]    # Intersting way to modify a string, slice (excluding the char you are replacing) and add the char you are replacing it with in the middle of the slices        
    return grid



        

