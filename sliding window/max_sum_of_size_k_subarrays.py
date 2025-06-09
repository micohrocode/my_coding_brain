def max_subarray_sum(nums, k):
    max_sum = 0
    state = 0
    start = 0

    for end in range(len(nums)):
        # store the total in state
        state+=nums[end]

        # if the k size is reached
        if end - start + 1 == k:
            # check for a new max sum
            max_sum = max(max_sum, state)
            # shrink the window by one
            state -= nums[start]
            start += 1
    
    return max_sum