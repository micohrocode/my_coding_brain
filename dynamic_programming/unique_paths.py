def unique_paths(m,n):
    # array of dimensions size
    dp = [[0]*n for _ in range(m)]

    # only one way to reach top row
    # only moving right
    for i in range(n):
        dp[0][i]=1

    # only one way to reach cells in first column
    # only moving down
    for j in range(m):
        dp[j][0] = 1

    # fill the rest
    for i in range(1,m):
        for j in range(1,n):
            # check the box above and left of it
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]