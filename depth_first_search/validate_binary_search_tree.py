def validateBST(root):
    def dfs(node, min_, max_):
        # end of path
        if node is None:
            return True
        
        # node value falls of out allowed range
        if node.val <= min_ or node.val >=max:
            return False
    
        # check left and right nodes
        return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)
    
    # initial call for root
    return dfs(root, float('-inf'), float('inf'))