def findTilt(root):
    # var to be passed down as needed
    tilt = 0
    def dfs(node):
        nonlocal tilt

        if not node:
            return 0

        # calc the tilt of the left and right 
        left = dfs(node.left)
        right = dfs(node.right)

        # add the tilt
        tilt+= abs(left-right)

        return left+right+node.val
    
    dfs(root)
    return tilt