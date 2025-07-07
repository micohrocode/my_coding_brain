def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1,len(s)+1):
        # for all letters before it
        for j in range(i):
            # check the substring
            sub = s[j:i]
            # if the letter at j
            # and the current substring is True
            # dp[i] is set to True
            if dp[j] and sub in wordSet:
                dp[i] = True
                break
    
    return dp[len(s)]