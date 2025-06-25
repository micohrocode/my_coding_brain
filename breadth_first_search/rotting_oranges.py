from collections import deque

def rotting_oranges(grid):
    if not grid:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "R":
                # find all rotten oranges
                queue.append((r,c))
            elif grid[r][c] == "F":
                # count all fresh oranges
                fresh_oranges+=1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    minutes = 0

    while queue and fresh_oranges > 0:
        # a minute passes
        minutes += 1

        # process all now rotting oranges for this minute
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "F":
                    # mark the orange as rotten
                    # add it to the queue
                    grid[nx][ny] = "R"
                    fresh_oranges -= 1
                    queue.append((nx,ny))
    
    return minutes if fresh_oranges == 0 else -1