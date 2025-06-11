def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # check if its a closing paren
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                # if there is no open paren
                # or the most recent one doesnt match
                return False
            # else remove the open paren
            stack.pop()
        else:
            # add the open paren
            stack.append(char)
    
    return len(stack) == 0
        