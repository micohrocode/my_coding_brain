from collections import deque


def maxWidth(root):
    if not root:
        return 0
    
    queue = deque[(root,0)]
    max_ = 0

    while queue:
        level_size = len(queue)

        _, leftPos  = queue[0]
        rightPos = -1

        for i in range(level_size):
            node, pos = queue.popleft()

            # last node of level was reached
            if i == level_size - 1:
                rightPos = pos

            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        max_ = max(max_, rightPos - leftPos + 1)

    return max_