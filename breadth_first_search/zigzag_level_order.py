from collections import deque

def zig_zag(root):
    if not root:
        return []
    
    nodes = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        nodes_for_level = deque()

        # process all nodes at the current level
        for i in range(level_size):
            node = queue.popleft()

            if left_to_right:
                # add to the back
                nodes_for_level.append(node.val)
            else:
                nodes_for_level.appendleft(node.val)
        
            # check for left and right nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        nodes.append(list(nodes_for_level))
        # switch directions
        left_to_right = not left_to_right

    return nodes