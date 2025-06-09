def maxScore(cards, k):
    # get the total sum of all cards
    total = sum(cards)
    # if k is larger than the cards available
    if k >= len(cards):
        return total
    
    state = 0
    max_points = 0
    start = 0

    for end in range(len(cards)):
        # add the new end to the current total
        state += cards[end]

        # if the window matches
        if end - start + 1 == len(cards) - k:
            # check for a new max total
            max_points = max(total - state, max_points)
            # shrink the window
            state -= cards[start]
            start += 1
    
    return max_points