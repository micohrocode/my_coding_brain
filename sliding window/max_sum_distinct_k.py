def maxSum(nums, k):
    max_sum = 0
    start = 0
    state = {}
    curr_sum = 0

    for end in range(len(nums)):
        # add new end to the current total
        curr_sum = curr_sum + nums[end]
        # update the state
        state[nums[end]] = state.get(nums[end],0) + 1

        # if the window is of size k
        if end - start + 1 == k:
            if len(state) == k:
                # if they are all unique
                # check for new max
                max_sum = max(max_sum, curr_sum)
            
            # update sum and state
            # shrink the window
            curr_sum = curr_sum - nums[start]
            state[nums[start]] = state[nums[start]] - 1
            if state[nums[start]] == 0:
                del state[nums[start]]
            start += 1
    
    return max_sum