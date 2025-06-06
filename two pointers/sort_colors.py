def sortColors(nums):
    left, right = 0, len(nums) - 1
    i = 0

    while i<=right:
        if nums[i] == 0:
            # if i is a zero, swap left and i values
            # move the pointers
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            # if i is a two, swap right and i values
            # move pointer
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            # no swaps needed
            i += 1

    return nums