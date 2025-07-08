def canJump(nums):
    # the furthest that can currently
    # be reached
    max_reach = 0
    for i in range(len(nums)):
        if i>max_reach:
            # if this cant be reached
            # by something before it
            # then False
            return False
        # check new max reach
        max_reach = max(max_reach, 1 + nums[i])
    return True