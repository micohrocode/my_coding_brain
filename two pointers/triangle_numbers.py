def triangleNumber(nums):
    nums.sort()

    count = 0

    # start at the end and move down
    for i in range(len(nums)-1,1,-1):
        left = 0
        right = i - 1

        while left < right:
            # check if two smaller sides added
            # are greater than the large side
            if nums[left] + nums[right] > nums[i]:
                # if so all triangles afer that
                # are valid
                count += right - left
                right -=1 
            else:
                left += 1
        
    return count
