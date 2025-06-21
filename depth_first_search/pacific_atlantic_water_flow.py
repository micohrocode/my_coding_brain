def pacific_atlantic_flow(grid):
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])

    # initialize empty sets
    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs(r,c, reachable):
        # add point to the reachable set
        reachable.add((r,c))
        # check all directions for water flow
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            # if its in bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                # and point is not already reached
                # and is greater than the current point
                if (nr, nc) not in reachable and grid[nr][nc] >= grid[r][c]:
                        # search from new point
                        dfs(nr, nc, reachable)
    
    for r in range(rows):
        dfs(r, 0, pacific_reachable)
        dfs(r, cols - 1, atlantic_reachable)

    for c in range(cols):
        dfs(0, c, pacific_reachable)
        dfs(rows - 1, c, atlantic_reachable)
    
    return list(pacific_reachable & atlantic_reachable)
         