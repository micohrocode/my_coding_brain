def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    i = 0

    while i < len(heights):
        # push to the stack as long as it
        # keep increasing
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i+=1
        else:
            # when it stops increasing
            # take tallest one
            top = stack.pop()
            # find the current right side
            right = i - 1
            # find the current left side
            left = stack[-1] if stack else -1
            # test for a new largest area
            area = heights[top] * (right-left)
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = i - stack[-1] - 1  if stack else i
        area = heights[top] * width
        max_area = max(max_area, area)

    return max_area