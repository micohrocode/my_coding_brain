from collections import deque


def updateMatrix(mat):
    rows, cols = len(mat), len(mat[0])
    output = [[-1](cols) for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                # mark all spots that have zeros
                queue.append((r,c))
                output[r][c] = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    distance = 1
    while queue:
        for _ in range(len(queue)):
            r,c = queue.popleft()

            for dr, dc in directions:
                # check every direction
                nr, nc = r+dr, c+dc

                if 0<=nr<rows and 0<=nc<cols:
                    # for ever -1 found
                    if output[nr][nc] == -1:
                        # update the distance
                        output[nr][nc] = distance
                        queue.append((nr,nc))
        # move to the next level
        distance +=1

    return output

