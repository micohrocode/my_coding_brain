def twoSum(nums, target):
    # pointers are set
    left, right = 0, len(nums) - 1
        
    # while the pointers have not met
    while left < right:
        # check the current sum
        current_sum = nums[left] + nums[right]
        # see if the current sum is equal to the target
        if current_sum == target:
            return True

        # if too low, move the left pointer up
        # to a higher number
        if current_sum < target:
            left += 1
        else:
            # else if too high
            # move right down to a lower number
            right -= 1
        
    return False