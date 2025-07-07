def maximal_square(matrix):
    if not matrix:
        return 0
    
    r = len(matrix)
    c = len(matrix[0])
    # extra space to calc side length
    # for outside row and column
    dp  = [[0] (c+1) for _ in range(r+1)]
    max_side = 0

    for i in range(1, r+1):
        for j in range(1, c+1):
            if matrix[i-1][j-1] == 1:
                # check the square directions
                top = dp[i-1][j]
                left = dp[i][j-1]
                diag = dp[i - 1][j - 1]
                # if all are 1+
                # then this square gets a higher number
                dp[i][j] = min(top, left, diag) + 1
                # check for new max side
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side