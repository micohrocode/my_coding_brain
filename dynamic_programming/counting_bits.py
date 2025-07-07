def count_bits(n):
    dp = [0] * (n+1)

    for i in range(1, n+1):
        # each item is made up of
        # the 1s located in i//2
        # and its rightmost bit
        dp[i] = dp[i//2] + (i%2)

    return dp