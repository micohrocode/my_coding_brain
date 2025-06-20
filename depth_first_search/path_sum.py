def hasPathSum(root, target):
    # end of the path, false
    if not root:
        return False
    
    # if it is a leaf, check the path total
    if not root.left and not root.right:
        return target == root.val
    
    # check left and right nodes
    left = hasPathSum(root.left, target - root.val)
    right = hasPathSum(root.right, target - root.val)
    return left or right