def characterReplacement(s, k):
    state = {}
    max_freq = 0
    max_length = 0
    start = 0

    for end in range(len(s)):
        # add the end of new substring to the state
        state[s[end]] = state.get(s[end],0) + 1
        # check for a new max with the added letter
        max_freq = max(max_freq, state[s[end]])

        # check if there are enough replacements for it to work
        if k + max_freq < end - start + 1:
            # if not shrink the window
            state[s[start]] -= 1
            start += 1
        
        # check for a new max length substring
        max_length = max(max_length, end - start + 1)

    return max_length