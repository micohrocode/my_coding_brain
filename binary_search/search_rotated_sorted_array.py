def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid]==target:
            return mid
        if nums[left]<= nums[mid]:
            # left is the sorted half
            # if the target is greater than the left pointer
            # but smaller than the mid point
            # than it is in the left side
            if nums[left]<= target and target < nums[mid]:
                right =  mid - 1
            else:
                # else its in the right side
                left =  mid + 1
        else:
            # if the target is greater than the middle
            # and less than the right
            # then it is on the right side
            if nums[mid] < target and target <= nums[right]:
                left =  mid + 1
            else:
                # else its on the lest
                right =  mid - 1

    # not found
    return -1