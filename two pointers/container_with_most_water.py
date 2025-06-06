def max_area(heights):
    # set the pointers
    left, right = 0, len(heights) - 1
    # current max area rectangle found
    current_max = 0

    while left < right:
        # width of rectangle from the indexs
        width = right - left
        # height of water
        height = min(heights[left], heights[right])
        current_area = width * height

        # check if new max
        current_max = max(current_max, current_area)

        # always move the box to check for higher water levels
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return current_max