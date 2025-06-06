def threeSum(nums):
    nums.sort()
    result = set()

    # for sets of three
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            # check the total of the three
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                # if too small, check higher
                left += 1
            elif total > 0:
                # if too high, check smaller
                right -=1
            else:
                result.add([nums[i],nums[left],nums[right]])
            
            # check for duplicates and move past them
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            # move the pointers
            left += 1
            right -= 1

    return result

