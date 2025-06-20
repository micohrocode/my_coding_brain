def diameterOfBinaryTree(root):
    max_ = 0

    def dfs(node):
        nonlocal max_
        if not node:
            return 0
        
        # get the max depth of the left and right
        # subrtrees
        left = dfs(node.left)
        right = dfs(node.right)

        # set the new max
        max_ = max(max_, left + right)

        # add one to the max depth to 
        # include the current node
        return max(left, right) + 1
    
    dfs(root)
    return max_