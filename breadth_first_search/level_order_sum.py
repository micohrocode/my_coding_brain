from collections import deque


def levelSum(root):
    if not root:
        return []
    
    nodes = []
    queue = deque([root])

    while queue:
        # new level here
        level_size = len(queue)
        sum_ = 0

        # all nodes in current level
        for i in range(level_size):
            # take a node from the queue
            node = queue.popleft()
            # add its value
            sum_ += node.val

            # search the left and right for nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # add the sum for the level
        nodes.append(sum_)
    
    return nodes