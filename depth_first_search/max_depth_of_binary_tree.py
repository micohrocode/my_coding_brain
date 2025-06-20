def maxDepth(root):
    # end of the line? dont add anything
    if root is None:
        return 0
    
    # find the max of the left and right
    left = maxDepth(root.left)
    right = maxDepth(root.right)

    # add one for the current node to that max
    return max(left,right) + 1