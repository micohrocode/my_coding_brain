def decodeString(s):
    stack = []
    curr_string = ""
    current_number = 0

    for char in s:
        if char == "[":
            # if its an open bracket
            # add the current string and number
            stack.append(curr_string)
            stack.append(current_number)
            # then reset them
            curr_string = ""
            current_number = 0
        elif char == "]":
            # if its a closing bracket
            # take the prev num and string and 
            # add them to the current string
            num = stack.pop()
            prev_string = stack.pop()
            curr_string = prev_string + num * curr_string
        elif char.isdigit():
            # add the digit to the number
            current_number = current_number * 10 + int(char)
        else:
            # add to the current string
            curr_string += char
    
    return curr_string