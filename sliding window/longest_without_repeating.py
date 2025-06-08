def longestWithoutRepeating(s):
    seen = {}
    max_length = 0
    # the left side that is contracted as needed
    start = 0

    for end in range(len(s)):
        # add the ending letter to what can be seen
        # in the current window
        seen[s[end]] = seen.get(s[end],0) + 1

        # if there are duplicates
        while seen[s[end]]>1:
            # remove them
            seen[s[start]] -= 1
            # and contract the window
            start += 1

        max_length = max(max_length, end - start + 1)
    
    return max_length