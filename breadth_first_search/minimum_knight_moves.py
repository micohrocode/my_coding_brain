from collections import deque

def minimum_knight_moves(x,y):
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                  (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    queue = deque([(0,0,0)])
    visited = set((0,0))

    while queue:
        # current position
        cx,cy,moves = queue.popleft()

        # reached the destination
        if (cx,cy) == (x,y):
            return moves
        
        # check all possible moves
        for dx,dy in directions:
            nx, ny = cx+dx, cy+dy

            # if the new positiopn is not visited yet
            # add it to the queue, mark it as visited
            # and increment the number of moves
            if (nx, ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny, moves+1))
    
    return -1