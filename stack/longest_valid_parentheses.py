def longest_valid_parentheses(s):
    max_len = 0
    # -1 for start of first valid
    stack = [-1]

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            # remove the last open paren
            stack.pop()
            if not stack:
                # stack is empty, update the start
                # of the valid substring
                stack.append(i)
            else:
                # stack is not empty
                # calculate lenght of valid substing
                max_len = max(max_len, i-stack[-1])
    
    return max_len