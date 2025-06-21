def flood_fill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == color:
        return image
    
    def dfs(r, c):
        # if it matches the original color
        # change it to the new color
        if image[r][c] == original_color:
            image[r][c] = color
        
        # check all four directions
        if r>=1: dfs(r-1, c)
        if r+1 < rows: dfs(r+1, c)
        if c>=1: dfs(r, c-1)
        if c+1 < cols: dfs(r, c+1)
        return
    
    dfs(sr, sc)
    return image