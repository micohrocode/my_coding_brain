def subarraySum(nums, k):
    # total number of subarrays that
    # sum up to k
    count = 0
    # sum up to current index
    sum_ = 0
    prefix_counts = {0: 1}

    for num in nums:
        # sum up to current index
        sum_ += num
        if sum_ - k in prefix_counts:
            # coutn subarrays that sum to k
            count+= prefix_counts[sum_ - k]
        
        # update prefix counts
        prefix_counts[sum_] = prefix_counts.get(sum_, 0) + 1
    
    return count
