def spiral_order(matrix):
    result = []

    while matrix:
        # get the top row first
        result += matrix.pop(0)

        # get the right column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # get the bottom row
        if matrix:
            result += matrix.pop()[::-1]
        
        # get the left column
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
        
        # repeat as needed
    
    return result