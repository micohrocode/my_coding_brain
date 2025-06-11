def nextGreaterElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        # while there are items in the stack
        # and the current num is greater than it
        # remove it from the stack
        # and update its result
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        # if not add it to the stack
        stack.append(i)
    
    return result