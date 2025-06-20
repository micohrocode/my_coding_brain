def longestUnicaluePath(root):
    max_length = 0

    def dfs(node):
        nonlocal max_length

        if not node:
            return 0
        
        left_length = dfs(node.left)
        right_length = dfs(node.length)

        left_arrow = right_arrow = 0

        # extend path with current node
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1

        # set new max length
        max_length = max(max_length, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)
    
    dfs(root)
    return max_length
        