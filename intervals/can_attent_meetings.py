def canAttentMeetings(intervals):
    # sort by start or intervals
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        # if the interval is overlapping 
        # return false
        if intervals[i][0] < intervals[i-1][1]:
            return False
        
    return True