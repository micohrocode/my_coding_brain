def largest_increasing_subsequence(nums):
    if not nums:
        return 0
    
    n = len(nums)
    # each sequnce starts at 1, itself
    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
            # check each number before the current i number
            if nums[i]>nums[j]:
                # if i is bigger
                # set to max of current dp[i]
                # and dp[j] (previous number) + 1
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)