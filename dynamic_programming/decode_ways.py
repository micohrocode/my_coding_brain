def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n+1)
    # only one way for an empty 
    # string and the first digit
    dp[0], dp[1] = 1,1

    for i in range(2, n+1):
        # check single digit
        digit = int(s[i-1])

        # if not zero add to possible decodings
        if digit!=0:
            dp[i] += dp[i-1]

        # check double digits
        digit = int(s[i-2:i])
        if 10<=digit<=26:
            # if valid number
            # add to possible decodings
            dp[i] += dp[i - 2]

    return dp[n]