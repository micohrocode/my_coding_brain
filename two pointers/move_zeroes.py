def moveZeroes(nums):
    nextNonZero = 0
    for i in range(len(nums)):
        # found a non zero?
        if nums[i] != 0:
            # swap the zero and nonZero
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
            nextNonZero += 1