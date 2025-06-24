from collections import deque


def rightmosstNode(root):
    if not root:
        return []
    
    nodes = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            # remove the first node
            node = queue.popleft()

            # check if rightmost
            if i == level_size - 1:
                nodes.append(node.val)
            
            # check nodes on left and right
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return nodes