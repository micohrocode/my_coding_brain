def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        # check if this is the correct length
        if index == len(word):
            return True
        # check if it is out of bounds or the wrong letter
        if r < 0 or c < 0 or r>= rows or c >=cols or board[r][c] != word[index]:
            return False

        # mark the grid item as seen
        temp = board[r][c]
        board[r][c] = "#"


        # check all surround directions
        found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

        # set back to the letter
        board[r][c] = temp
        # return if the next letter is found
        return found
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:
                if dfs(row, col, 0):
                    return True
    
    return False