def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    # mark all rows and cols to be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for row in zero_rows:
        for col in range(cols):
            # set all rows to zero
            matrix[row][col] = 0
    
    for col in zero_cols:
        for row in range(rows):
            # set all columns to zero
            matrix[row][col] = 0
    
    return matrix