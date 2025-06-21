def surrounded_regions(grid):
    if not grid:
        return grid
    
    rows = len(grid)
    cols = len(grid)

    def dfs(x,y):
        if x<0 or y<0 or x>=rows or y>=cols or grid[x][y]!='O':
            return
        grid[x][y] = 'S'

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    # dfs for first and last column
    for i in range(rows):
        if grid[i][0] == 'O':
            dfs(i, 0)
        if grid[i][cols-1] == 'O':
            dfs(i, cols-1)
    
    # dfs for first and last row
    for j in range(cols):
        if grid[0][j] == 'O':
            dfs(0,j)
        if grid[rows-1][j] == 'O':
            dfs(rows-1,j)

    # change Os not marked to Xs
    # change Ss back to Os
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                grid[i][j] = "X"
            elif grid[i][j] == 'S':
                grid[i][j] = 'O'
                    
    return grid
    
    
