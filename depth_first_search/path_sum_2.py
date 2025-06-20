def pathSum(root, target):
    def dfs(node, target, path):
        if not node:
            return
        
        # keep track of the current path
        path.append(node.val)
        # if its a lead node
        if not node.left and not node.right:
            # and equal to the target
            if node.val == target:
                # add the path to the result
                result.append(path[:])

        # check left and right path
        dfs(node.left, target-node.val, path)
        dfs(node.right, target - node.val, path)
        # remove from path
        path.pop()

        result = []
        dfs(root, target, [])
        return result