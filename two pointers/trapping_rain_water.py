def trappingWater(heights):
    left, right = 0, len(heights) - 1
    leftMax, rightMax = heights[left], heights[right]

    count = 0

    while left + 1 < right:
        # if left max is the lower side
        if rightMax > leftMax:
            # move left pointer first
            left += 1

            # if new max then update it
            if heights[left]>leftMax:
                leftMax = heights[left]
            else:
                # else calc the trapped water
                count += leftMax - heights[left]
        else:
            # right is the lower side
            # so move right first
            right -= 1
            if heights[right] > rightMax:
                # if new right max update its
                rightMax = heights[right]
            else:
                # else, calc the trapped water
                count += rightMax - heights[right]
    
    return count