def insertIntervals(intervals, newInterval):
    merged = []
    i = 0
    n = len(intervals)

    # for intervals that end before the new one
    # that is added
    while i<n and intervals[i][1] < newInterval[0]:
        # add them to the result
        merged.append(intervals[i])
        # move to the next one
        i+=1

    while i<n and intervals[i][0] <= newInterval[1]:
        # merge the two intervals
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        # move to the next interval
        i += 1
    
    merged.append(newInterval)
    # add the rest of the intervals
    for j in range(i, n):
        merged.append(intervals[j])

    return merged